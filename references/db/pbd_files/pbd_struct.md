# 标准接口-pbd_struct

## 输出对象字段-子表 t_pbd_struct_outputentity

- **表名称：** 输出对象字段-子表
- **表名：** t_pbd_struct_outputentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutputsfieldname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 3 | foutputskeystatus | 字段状态 | varchar | 50 |  | √ | ' ' | 字段状态,枚举: PU :系统预置未修改 PM :系统预置已修改 NEW :新增字段 |
| 4 | foutputskeyisv | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 5 | foutputsfieldid | 字段标识 | varchar | 80 |  | √ | ' ' | 字段标识 |
| 6 | foutputsfieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :是/否 ENUM :枚举 STRUCT :结构 basedatafield :基础资料 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 9 | foutputsisarray | 是否多值 | bpchar | 1 |  | √ | '0' | 是否多值 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_struct_out_fid_fseq |  | fid,fseq |
| 2 | pk_pbd_struct_outputentity |  | fentryid |

---

## 输入对象字段-子表 t_pbd_struct_inputentity

- **表名称：** 输入对象字段-子表
- **表名：** t_pbd_struct_inputentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finputsisarray | 是否多值 | bpchar | 1 |  | √ | '0' | 是否多值 |
| 3 | finputsfieldid | 字段标识 | varchar | 80 |  | √ | ' ' | 字段标识 |
| 4 | finputsfieldname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 5 | finputsfieldtype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: string :字符串 int :整数 decimal :小数 datetime :日期/时间 long :长整数 boolean :是/否 ENUM :枚举 STRUCT :结构 basedatafield :基础资料 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | finputskeyisv | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 10 | finputskeystatus | 字段状态 | varchar | 50 |  | √ | ' ' | 字段状态,枚举: PU :系统预置未修改 PM :系统预置已修改 NEW :新增字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_struct_inputentity |  | fentryid |
| 2 | idx_pbd_struct_input_fid_fseq |  | fid,fseq |

---

## 标准接口-多语言表 t_pbd_struct_l

- **表名称：** 标准接口-多语言表
- **表名：** t_pbd_struct_l

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
| 1 | idx_pbd_struct_l_fid |  | fid |
| 2 | pk_pbd_struct_l |  | fpkid |

---

## 标准接口-主表 t_pbd_struct

- **表名称：** 标准接口-主表
- **表名：** t_pbd_struct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 接口描述 | varchar | 1000 |  | √ | ' ' | 接口描述 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fispreinsdata | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsourceid | 外部数据元数据库 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 1 :实体 2 :结构 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fentitycode | 元数据 | varchar | 512 |  | √ | ' ' | 元数据,枚举: |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_struct_fnumber |  | fnumber |
| 2 | pk_pbd_struct |  | fid |
