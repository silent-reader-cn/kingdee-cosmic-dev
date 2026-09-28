# 离线数据源-didc_ods

## 离线数据源-多语言表 t_didc_ods_l

- **表名称：** 离线数据源-多语言表
- **表名：** t_didc_ods_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 数据源名称 | varchar | 50 |  | √ | ' ' | 数据源名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_ods_l |  | fid |
| 2 | pk_t_didc_ods_l |  | fpkid |

---

## 字段元数据-子表 t_didc_fieldmeta

- **表名称：** 字段元数据-子表
- **表名：** t_didc_fieldmeta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdisplayname | 显示名称 | varchar | 255 |  | √ | ' ' | 显示名称 |
| 3 | ffieldtype | 数据类型 | varchar | 255 |  | √ | ' ' | 数据类型,枚举: TEXT :文本 NUM :数值 DATE :日期 |
| 4 | fcsvfieldname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 5 | ffieldname | 字段编码 | varchar | 255 |  | √ | ' ' | 字段编码 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_didc_fieldmeta |  | fentryid |
| 2 | idx_didc_fieldmeta |  | fid |

---

## 离线数据源-主表 t_didc_ods

- **表名称：** 离线数据源-主表
- **表名：** t_didc_ods

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 数据源名称 | varchar | 255 |  | √ | ' ' | 数据源名称 |
| 3 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 8 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 9 | fnumber | 数据源编码 | varchar | 30 |  | √ | ' ' | 数据源编码 |
| 10 | ftablename | 数据存储表名 | varchar | 255 |  | √ | ' ' | 数据存储表名 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_ods |  | fnumber |
| 2 | pk_t_didc_ods |  | fid |
