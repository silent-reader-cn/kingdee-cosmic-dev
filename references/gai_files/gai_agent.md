# 智能体-gai_agent

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
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | ftool | 编码 | int8 | 64 |  | √ | 0 | 插件 gai_tool |

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
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
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
| 3 | frepo | 编码 | int8 | 64 |  | √ | 0 | 知识库 gai_repo_info |
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
| 1 | fquestion | 问题 | varchar | 255 |  | √ | ' ' | 问题 |
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

## 智能体-主表 t_gai_agent

- **表名称：** 智能体-主表
- **表名：** t_gai_agent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentname | Agent标识 | varchar | 50 |  | √ | ' ' | Agent标识 |
| 3 | fuseorg | 使用组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fllmname | 语言模型名称 | varchar | 100 |  | √ | ' ' | 语言模型名称 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | froledesc | 角色及任务设定 | varchar | 255 |  | √ | ' ' | 角色及任务设定 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fpicture | 头像 | varchar | 255 |  | √ | ' ' | 头像 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | frolemode | 角色反应模式 | varchar | 50 |  | √ | ' ' | 角色反应模式,枚举: react :标准ReAct by_order :顺序执行 plan_and_act :规划执行 |
| 13 | froledesc_tag | 角色及任务设定_详情 | text | 0 |  |  | null | 角色及任务设定_详情 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fbgcolor | 背景颜色 | varchar | 50 |  | √ | ' ' | 背景颜色 |
| 17 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fllmstyle | 模型风格 | varchar | 50 |  | √ | ' ' | 模型风格,枚举: CREATIVITY :创意 BALANCE :平衡 PRECISION :精准 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 24 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fprologue | 引导语 | varchar | 255 |  | √ | ' ' | 引导语 |
| 26 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: custom :自定义 preset :系统 |
| 27 | fllm | 语言模型 | varchar | 50 |  | √ | ' ' | 语言模型,枚举: |
| 28 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 30 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 31 | fremembercount | 包含历史消息 | numeric | 12 |  | √ | 0 | 包含历史消息 |

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
| 3 | fquestion | 问题 | varchar | 255 |  | √ | ' ' | 问题 |
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

## 单据体-GPT提示-子表 t_gai_agent_prompt

- **表名称：** 单据体-GPT提示-子表
- **表名：** t_gai_agent_prompt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fprompt | 编码 | int8 | 64 |  | √ | 0 | GPT提示 gai_prompt |

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

## 智能体-多语言表 t_gai_agent_l

- **表名称：** 智能体-多语言表
- **表名：** t_gai_agent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fprologue | 引导语 | varchar | 255 |  | √ | ' ' | 引导语 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_agent_l |  | fpkid |
| 2 | idx_gai_assistant_l_fname |  | fname |

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
| 4 | fprocess | 编码 | int8 | 64 |  | √ | 0 | 任务流 gai_process |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_agent_process |  | fentryid |
| 2 | idx_gai_assistant_process_fid |  | fid |
