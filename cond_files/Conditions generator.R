# load packages
library(tidyverse)
# set path to where the script is
this.path::here() 

# PARAMETERS --------------------------------------------------------------

# specify task parameters
factors <- c("angle", "laterality", "view")  # names of factors
#levels of factors
angle <- c(0, 90, 180, 270)
laterality <- c("left", "right")
view <- c("dorsal", "palmar")
unique_conditions <- length(angle) * length(laterality) * length(view)
# timings for forced response, in ms
timing <- seq(20, 2000, by = 20)
#total trials in experiment
total_trials <- unique_conditions * length(timing)
# based on the total trials and duration of each trial, set block params
block_trials = 160
block <- 1:(total_trials / block_trials)
# folder in PsychoPy big folder where the actual files for the stimuli actually are
stim_folder = "stimuli"

# create condition grid
conditions <- expand.grid(angle = angle,
                          laterality = laterality,
                          view = view,
                          timing = timing) |>
  # now add the actual file and correct key for PsychoPy
  mutate(file = case_when(laterality == "left" & view == "dorsal" ~ paste0(stim_folder, "/left_dorsal.png"),
                          laterality == "left" & view == "palmar" ~ paste0(stim_folder, "/left_palmar.png"),
                          laterality == "right" & view == "dorsal" ~ paste0(stim_folder, "/right_dorsal.png"),
                          laterality == "right" & view == "palmar" ~ paste0(stim_folder, "/right_palmar.png")),
         correct_key = ifelse(laterality == "left", "s", "l"))


# FUNCTION TO SPLIT CONDITIONS IN BLOCKS ----------------------------------------------------------------

# define custom function to distribute conditions with balanced distributions of timings per block
# equal number of factors per block
# equal number of combinations
split_cond <- function(conditions = NULL, # grid with conditions
                      factors = NULL, #
                      n_blocks = NULL, # number of blocks
                      block_trials = NULL, # number of trials per block
                      timings_block = NULL # unique timings per block per combination of factor
                      ){

  # add unique row id
  conditions <- conditions |>
    arrange(timing) |>
    group_by(across(all_of(factors))) |>
    mutate(timing_group = ntile(timing, timings_block)) |>
    ungroup() |>
    mutate(row_id = row_number())

  # initialize pool of available rows
  remaining <- conditions

  # sample remaining rows and select 1 at a time
  blocks <- vector("list", length = n_blocks)
  for (i in seq_len(n_blocks)) {
    # sample 1 trial per combi × timing_group from remaining
    blk <- remaining |>
      group_by(across(all_of(c(factors, "timing_group")))) |>
      slice_sample(n = 1) |>
      ungroup()

    # remove those rows
    remaining <- anti_join(remaining, blk, by = "row_id")
    # assign to list
    blk$block <- i
    blocks[[i]] <- blk
  }

  # return list of data frames
  blocks
}

# RUN FUNCTION -----------------------------------------

blocks_list <- split_cond(
  conditions = conditions,
  factors = c("angle", "laterality", "view"),
  n_blocks = 10,
  block_trials = 160,
  timings_block = 10  # timings per unique combination of factor
  )


# CONFIRM SPLIT IS CORRECT ------------------------------------------------

d <- bind_rows(blocks_list) |>
  mutate(window = cut(timing,
                      breaks = seq(0, 2000, by = 200),
                      labels = FALSE,
                      right = FALSE))
ggplot(d, aes(x = window, fill = factor(angle))) +
  geom_histogram() +
  facet_wrap(~block + view)


# FUNCTIONS TO SHUFFLE WITH RESTRICTIONS -----------------------------------

# custom function to shuffle each block with a maximum number of consecutive repetitions per factor
shuffle_block <- function(block,
                          factors,
                          max_reps = 4,
                          max_attempts = 10^6
                          ) {
  check_runs <- function(x) max(rle(as.character(x))$lengths) <= max_reps

  for (i in seq_len(max_attempts)) {
    block_shuffled <- block[sample(nrow(block)), ]
    ok <- vapply(factors, function(f) check_runs(block_shuffled[[f]]), logical(1))
    if (all(ok)) return(block_shuffled)
  }

  stop("No valid solution with this max_attempts.")
}

# custom function to check if the the randomisation was successful
check_max_reps <- function(df,
                           factors,
                           max_reps
                           ) {
  purrr::map_lgl(factors, function(f) {
    max(rle(as.character(df[[f]]))$lengths) <= max_reps
  })
}

# LOOP THROUGH THE BLOCKS (MAY TAKE A WHILE) -------------------------------------------------
max_reps <- 4  # with a combination of factors with 2 levels each, less than this is almost impossible to achieve
max_attempts <- 10^7

# shuffle
shuffled_blocks <- purrr::map(blocks_list, ~ shuffle_block(.x, factors = factors, max_reps = max_reps, max_attempts = max_attempts))

# check
purrr::map(shuffled_blocks, check_max_reps, factors = factors, max_reps = max_reps)


# WRANGLE ACCORDING TO PSYCHOPY EXPERIMENT VARIABLES -------------------------

final_blocks <- map(shuffled_blocks, function(df) {
  df |>
    mutate(timing = 2 - (timing/1000)) |> # transform to seconds and subtract from time of last tone in PsychoPy
    rename_with(~ paste0("stim_", .x), all_of(c("angle", "laterality", "view", "timing", "file", "correct_key"))) |>
    select(starts_with("stim"))
})


# EXPORT AS CSV --------------------------------------------------
purrr::iwalk(final_blocks, ~ {
  write_csv(.x, file = paste0("task_block", .y, ".csv"))
})


# RANDOMIZE PRACTICE CONDITIONS AND RE-EXPORT -------------------------------------------

pract_cond <- read_csv("cond_practice.csv")

pract_cond_random <- pract_cond[sample(nrow(pract_cond)), ]

write_csv(pract_cond_random, "cond_practice.csv")

