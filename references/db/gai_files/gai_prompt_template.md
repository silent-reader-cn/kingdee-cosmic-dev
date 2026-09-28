# 提示词模板-gai_prompt_template

## 提示词模板-主表 t_gai_prompt_template

- **表名称：** 提示词模板-主表
- **表名：** t_gai_prompt_template

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [提示词模板分组 gai_prompt_temp_group](../gai_files/gai_prompt_temp_group.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbusinessassistant | 业务助手 | bpchar | 1 |  | √ | '0' | 业务助手 |
| 5 | fisdraft | 草稿 | bpchar | 1 |  | √ | '0' | 草稿 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fispreset | 预置 | varchar | 1 |  | √ | '0' | 预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcustomstyle | 自定义风格 | varchar | 255 |  | √ | ' ' | 自定义风格 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 15 | fprompt | 提示词 | varchar | 255 |  | √ | ' ' | 提示词 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flanguagemodel | 语言模型 | varchar | 50 |  | √ | ' ' | 语言模型,枚举: |
| 21 | fcurrency | 通用 | bpchar | 1 |  | √ | '0' | 通用 |
| 22 | fdevassistant | 开发助手 | bpchar | 1 |  | √ | '0' | 开发助手 |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  |  | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fprompt_tag | 提示词_详情 | text | 0 |  |  | null | 提示词_详情 |
| 25 | fisencrypted | 加密 | varchar | 1 |  | √ | '0' | 加密 |
| 26 | fservicename | 模型服务 | varchar | 50 |  | √ | ' ' | 模型服务 |
| 27 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fblgids | 许可分组ID | varchar | 512 |  | √ | ' ' | 许可分组ID |
| 29 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 30 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fdesc | 说明 | varchar | 100 |  |  | ' ' | 说明 |
| 32 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 33 | fremembercount | 包含历史消息 | numeric | 12 | 10 | √ | 0 | 包含历史消息 |
| 34 | fmodelstyle | 模型风格 | varchar | 50 |  | √ | ' ' | 模型风格,枚举: CREATIVITY :创意 BALANCE :平衡 PRECISION :精准 CUSTOM :自定义 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_prompt_template_createorg |  | fcreateorgid |
| 2 | idx_t_gai_prompt_template_master |  | fmasterid |
| 3 | idx_gai_prompttpl_n |  | fname |
| 4 | pk_t_gai_prompt_tpl |  | fid |

---

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

## 提示词模板-使用范围表 t_gai_prompt_template_u

- **表名称：** 提示词模板-使用范围表
- **表名：** t_gai_prompt_template_u

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
| 1 | pk_t_gai_prompt_template_u |  | fdataid,fuseorgid |
| 2 | idx_t_gai_prompt_template_u_uo |  | fuseorgid |

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

## 提示词模板-多语言表 t_gai_prompt_template_l

- **表名称：** 提示词模板-多语言表
- **表名：** t_gai_prompt_template_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gai_prompttpl_l_n |  | fname |
| 2 | pk_t_gai_prompt_tpl_l |  | fpkid |

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
