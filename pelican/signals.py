from blinker import signal

initialized = signal('pelican_initialized')
finalized = signal('pelican_finalized')
article_generate_preread = signal('article_generate_preread')
generator_init = signal('generator_init')
article_generate_context = signal('article_generate_context')
article_generator_init = signal('article_generator_init')
article_generator_finalized = signal('article_generate_finalized')

entry_generate_preread = signal('entry_generate_preread')
entry_generate_context = signal('entry_generate_context')
entry_generator_init = signal('entry_generator_init')
entry_generator_finalized = signal('entry_generate_finalized')

get_generators = signal('get_generators')
pages_generate_context = signal('pages_generate_context')
pages_generator_init = signal('pages_generator_init')
content_object_init = signal('content_object_init')
