# 提示词-gai_prompt

## 自定义变量-子表 t_gai_prompt_in_var

- **表名称：** 自定义变量-子表
- **表名：** t_gai_prompt_in_var

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvar | 参数 | varchar | 20 |  |  | ' ' | 参数 |
| 3 | fvartype | 参数类型 | varchar | 50 |  |  | ' ' | 参数类型,枚举: String :文本 Integer :数字 DateTime :日期/时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fvarname | 说明 | varchar | 20 |  |  | ' ' | 说明 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_prompt_in_var |  | fid |
| 2 | pk_t_gai_prompt_in_var |  | fentryid |

---

## 提示词-主表 t_gai_prompt

- **表名称：** 提示词-主表
- **表名：** t_gai_prompt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [提示词分组 gai_prompt_group](../gai_files/gai_prompt_group.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbusinessassistant | 业务助手 | bpchar | 1 |  |  | '0' | 业务助手 |
| 5 | fisdraft | 草稿 | bpchar | 1 |  | √ | '0' | 草稿 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fispreset | 预置 | varchar | 1 |  |  | '0' | 预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fprocessrefcount | 任务流引用 | int8 | 64 |  | √ | 0 | 任务流引用 |
| 10 | fstatus | 数据状态 | varchar | 50 |  |  | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fencrypt | 加解密密码 | varchar | 100 |  | √ | ' ' | 加解密密码 |
| 14 | fcustomstyle | 自定义风格 | varchar | 255 |  | √ | ' ' | 自定义风格 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fprompt | 提示词 | varchar | 255 |  |  | ' ' | 提示词 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 21 | fagentrefcount | 智能体引用 | int8 | 64 |  | √ | 0 | 智能体引用 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | flanguagemodel | 语言模型 | varchar | 50 |  |  | ' ' | 语言模型,枚举: |
| 24 | fcurrency | 通用 | bpchar | 1 |  |  | '0' | 通用 |
| 25 | fdevassistant | 开发助手 | bpchar | 1 |  |  | '0' | 开发助手 |
| 26 | fctrlstrategy | 控制策略 | varchar | 50 |  |  | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 27 | fisvisible | 是否可见 | bpchar | 1 |  | √ | '1' | 是否可见 |
| 28 | fprompt_tag | 提示词_详情 | text | 0 |  |  | ' ' | 提示词_详情 |
| 29 | fisencrypted | 加密 | varchar | 1 |  |  | '0' | 加密 |
| 30 | fservicename | 模型服务 | varchar | 100 |  | √ | ' ' | 模型服务 |
| 31 | fenable | 使用状态 | varchar | 50 |  |  | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fblgids | 许可分组ID | varchar | 512 |  | √ | '606' | 许可分组ID |
| 33 | fnumber | 编码 | varchar | 30 |  |  | ' ' | 编码 |
| 34 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fdesc | 说明 | varchar | 100 |  |  | ' ' | 说明 |
| 36 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 37 | fremembercount | 包含历史消息 | numeric | 12 | 10 | √ | 0 | 包含历史消息 |
| 38 | fmodelstyle | 模型风格 | varchar | 50 |  |  | ' ' | 模型风格,枚举: CREATIVITY :创意 BALANCE :平衡 PRECISION :精准 CUSTOM :自定义 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_prompt_createorg |  | fcreateorgid |
| 2 | idx_gai_userrg |  | fuseorgid |
| 3 | idx_t_gai_prompt_master |  | fmasterid |
| 4 | idx_gai_number |  | fnumber |
| 5 | pk_t_gai_prompt |  | fid |

---

## 输出变量-子表 t_gai_prompt_out_var

- **表名称：** 输出变量-子表
- **表名：** t_gai_prompt_out_var

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvar | 参数 | varchar | 20 |  |  | ' ' | 参数 |
| 3 | fvartype | 参数类型 | varchar | 50 |  |  | ' ' | 参数类型,枚举: String :文本 Integer :数字 DateTime :日期/时间 |
| 4 | foutjsonanalysis | 解析json | varchar | 1 |  |  | '1' | 解析json |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fvarname | 说明 | varchar | 100 |  | √ | ' ' | 说明 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_prompt_out_var |  | fid |
| 2 | pk_t_gai_prompt_out_var |  | fentryid |

---

## 提示词-多语言表 t_gai_prompt_l

- **表名称：** 提示词-多语言表
- **表名：** t_gai_prompt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_prompt_l |  | fpkid |
| 2 | idxt_gai_prompt_l |  | fid |

---

## 提示词-使用范围表 t_gai_prompt_u

- **表名称：** 提示词-使用范围表
- **表名：** t_gai_prompt_u

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
| 1 | pk_t_gai_prompt_u |  | fdataid,fuseorgid |
| 2 | idx_t_gai_prompt_u_uo |  | fuseorgid |

---

## 知识库配置-子表 t_gai_prompt_repo_config

- **表名称：** 知识库配置-子表
- **表名：** t_gai_prompt_repo_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  |  | ' ' | 名称 |
| 3 | frepotype | 知识库类型 | varchar | 50 |  |  | ' ' | 知识库类型,枚举: qa :文档问答 kd_code_gen :代码生成 |
| 4 | fstringnumber | fstringnumber | int8 | 64 |  | √ | 0 |  |
| 5 | frepoid | 编码 | int8 | 64 |  | √ | 0 | [知识库 gai_repo_info](../gai_files/gai_repo_info.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_pompt_repo_config |  | fid |
| 2 | pk_t_gai_prompt_repo_config |  | fentryid |
