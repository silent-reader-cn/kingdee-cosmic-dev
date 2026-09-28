# GPT操作-gai_operation

## GPT操作-主表 t_gai_operation

- **表名称：** GPT操作-主表
- **表名：** t_gai_operation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 50 |  |  | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fispreset | 是否预置 | varchar | 1 |  |  | ' ' | 是否预置 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fappid | appid | varchar | 50 |  |  | ' ' | appid |
| 8 | fpresetnumber | 预置操作编码 | varchar | 50 |  |  | ' ' | 预置操作编码 |
| 9 | fstatus | 数据状态 | varchar | 50 |  |  | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | foperationtype | 操作类型 | varchar | 50 |  |  | ' ' | 操作类型,枚举: 0 :前端 1 :后端 |
| 13 | fapp | 应用 | varchar | 36 |  |  | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 14 | faction | 操作名称 | varchar | 50 |  |  | ' ' | 操作名称 |
| 15 | fservicename | 类名 | varchar | 200 |  |  | ' ' | 类名 |
| 16 | fenable | 使用状态 | varchar | 50 |  |  | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 30 |  |  | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gai_operation |  | fnumber |
| 2 | pk_t_gai_operation |  | fid |

---

## GPT操作-多语言表 t_gai_operation_l

- **表名称：** GPT操作-多语言表
- **表名：** t_gai_operation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_operation_l |  | fpkid |
| 2 | idx_t_gai_operation_l |  | fid |

---

## 输入-子表 t_gai_operation_input

- **表名称：** 输入-子表
- **表名：** t_gai_operation_input

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finputname | 参数名 | varchar | 50 |  |  | ' ' | 参数名 |
| 3 | fisinput | 手工维护 | bpchar | 1 |  | √ | ' ' | 手工维护 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | finputvalue | 手工维护内容 | varchar | 600 |  | √ | ' ' | 手工维护内容 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | finputdesc | 描述 | varchar | 200 |  |  | ' ' | 描述 |
| 8 | finputtype | 参数类型 | varchar | 50 |  |  | ' ' | 参数类型,枚举: String :文本 Integer :数字 DateTime :日期/时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_operation_input |  | fentryid |
| 2 | idx_t_gai_operation_input |  | fid |

---

## 输出-子表 t_gai_operation_output

- **表名称：** 输出-子表
- **表名：** t_gai_operation_output

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutputdesc | 说明 | varchar | 200 |  |  | ' ' | 说明 |
| 3 | foutputtype | 参数类型 | varchar | 50 |  |  | ' ' | 参数类型,枚举: String :文本 Integer :数字 DateTime :日期/时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | foutputname | 参数名 | varchar | 50 |  |  | ' ' | 参数名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_operation_output |  | fentryid |
| 2 | idx_t_gai_operation_output |  | fid |
