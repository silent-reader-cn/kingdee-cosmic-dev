# 智能体-gai_agent

## 智能体-主表 t_gai_agent

- **表名称：** 智能体-主表
- **表名：** t_gai_agent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentname | Agent标识 | varchar | 50 |  | √ | ' ' | Agent标识 |
| 3 | fisupload | 支持上传附件 | bpchar | 1 |  | √ | '1' | 支持上传附件 |
| 4 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fllmname | 语言模型名称 | varchar | 100 |  | √ | ' ' | 语言模型名称 |
| 6 | frepoautocall | 自动调用 | int8 | 64 |  | √ | 1 | 自动调用 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | ffiledesc | 文件信息 | varchar | 255 |  |  | ' ' | 文件信息 |
| 9 | froledesc | 角色及任务设定 | varchar | 255 |  | √ | ' ' | 角色及任务设定 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fispreset | 是否预置 | varchar | 1 |  | √ | '0' | 是否预置 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fpicture | 头像 | varchar | 255 |  | √ | ' ' | 头像 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | finputtips | 输入框提示语 | varchar | 50 |  | √ | ' ' | 输入框提示语 |
| 17 | frolemode | 角色反应模式 | varchar | 50 |  | √ | ' ' | 角色反应模式,枚举: react :标准ReAct by_order :顺序执行 plan_and_act :规划执行 functioncall :FunctionCall |
| 18 | froledesc_tag | 角色及任务设定_详情 | text | 0 |  |  | null | 角色及任务设定_详情 |
| 19 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 20 | fmaxuploadnums | 最大文件数量 | int8 | 64 |  | √ | 10 | 最大文件数量 |
| 21 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 22 | fisnew | isnew | bpchar | 1 |  | √ | '0' | isnew |
| 23 | fbgcolor | 背景颜色 | varchar | 50 |  | √ | ' ' | 背景颜色 |
| 24 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 25 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 27 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fllmstyle | 模型风格 | varchar | 50 |  | √ | ' ' | 模型风格,枚举: CREATIVITY :创意 BALANCE :平衡 PRECISION :精准 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 31 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 32 | fisvisible | 是否可见 | bpchar | 1 |  | √ | '1' | 是否可见 |
| 33 | ffiletypes | 文件类型 | varchar | 255 |  |  | ' ' | 文件类型 |
| 34 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: custom :自定义 preset :系统 |
| 35 | fprologue | 引导语 | varchar | 255 |  | √ | ' ' | 引导语 |
| 36 | fllm | 语言模型 | varchar | 50 |  | √ | ' ' | 语言模型,枚举: |
| 37 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 39 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 40 | fremembercount | 包含历史消息 | numeric | 12 |  | √ | 0 | 包含历史消息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_agent |  | fid |
| 2 | idx_gai_agent_assistant_fname |  | fname |
| 3 | idx_t_gai_agent_master |  | fmasterid |
| 4 | idx_t_gai_agent_createorg |  | fcreateorgid |

---

## 开场推荐问法-子表 t_gai_agent_start

- **表名称：** 开场推荐问法-子表
- **表名：** t_gai_agent_start

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fquestion | 推荐问法 | varchar | 255 |  | √ | ' ' | 推荐问法 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_agent_assist_start_fid |  | fid |
| 2 | pk_t_gai_agent_start |  | fentryid |

---

## 智能体-多语言表 t_gai_agent_l

- **表名称：** 智能体-多语言表
- **表名：** t_gai_agent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fprologue | 引导语 | varchar | 255 |  | √ | ' ' | 引导语 |
| 4 | finputtips | 输入框提示语 | varchar | 50 |  | √ | ' ' | 输入框提示语 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_assistant_l_fname |  | fname |
| 2 | pk_t_gai_agent_l |  | fpkid |

---

## 智能体-使用范围表 t_gai_agent_u

- **表名称：** 智能体-使用范围表
- **表名：** t_gai_agent_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_agent_u_uo |  | fuseorgid |
| 2 | pk_t_gai_agent_u |  | fdataid,fuseorgid |

---

## 单据体-工具-子表 t_gai_agent_tool

- **表名称：** 单据体-工具-子表
- **表名：** t_gai_agent_tool

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fselected_tag | 已选择接口_详情 | text | 0 |  |  | null | 已选择接口_详情 |
| 4 | fselected | 已选择接口 | varchar | 255 |  | √ | ' ' | 已选择接口 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ftool | 编码 | int8 | 64 |  | √ | 0 | [工具 gai_tool](../gai_files/gai_tool.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_agent_tool |  | fentryid |
| 2 | idx_gai_assistant_tool_fid |  | fid |

---

## 应用-多选基础资料表 t_gai_agent_app

- **表名称：** 应用-多选基础资料表
- **表名：** t_gai_agent_app

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_agent_app |  | fpkid |
| 2 | idx_gai_agent_app_fid |  | fid |

---

## 单据体-知识库-子表 t_gai_agent_repo

- **表名称：** 单据体-知识库-子表
- **表名：** t_gai_agent_repo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | frepo | 编码 | int8 | 64 |  | √ | 0 | [知识库管理 aikm_knl_manager](../aikm_files/aikm_knl_manager.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_agent_repo |  | fentryid |
| 2 | idx_gai_agent_assist_repo_fid |  | fid |

---

## 开场推荐问法-多语言表 t_gai_agent_start_l

- **表名称：** 开场推荐问法-多语言表
- **表名：** t_gai_agent_start_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fquestion | 推荐问法 | varchar | 255 |  | √ | ' ' | 推荐问法 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_agent_start_l |  | fpkid |
| 2 | idx_gai_assist_start_l_id |  | fentryid |

---

## 单据体-GPT提示-子表 t_gai_agent_prompt

- **表名称：** 单据体-GPT提示-子表
- **表名：** t_gai_agent_prompt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fprompt | 编码 | int8 | 64 |  | √ | 0 | [提示词 gai_prompt](../gai_files/gai_prompt.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_agent_prompt |  | fentryid |
| 2 | idx_gai_assistant_prompt_fid |  | fid |

---

## 单据体-GPT任务-子表 t_gai_agent_process

- **表名称：** 单据体-GPT任务-子表
- **表名：** t_gai_agent_process

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fprocess | 编码 | int8 | 64 |  | √ | 0 | [任务流 gai_process](../gai_files/gai_process.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_agent_process |  | fentryid |
| 2 | idx_gai_assistant_process_fid |  | fid |
