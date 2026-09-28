# 统计分析报表关键字-qcqs_analyrptkey

## 统计分析报表关键字-主表 t_qcqs_analyrptkey

- **表名称：** 统计分析报表关键字-主表
- **表名：** t_qcqs_analyrptkey

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 关键字名称 | varchar | 150 |  | √ | ' ' | 关键字名称 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fsplittype | 分类 | varchar | 5 |  | √ | ' ' | 分类,枚举: A :横坐标 B :序列名 |
| 9 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 关键字编码 | varchar | 30 |  | √ | ' ' | 关键字编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcqs_analey_fcreatetime |  | fcreatetime |
| 2 | pk_qcqs_analyrptkey |  | fid |
| 3 | idx_qcqs_analey_fnumber |  | fnumber |

---

## 单据体-子表 t_qcqs_rptkeyentry

- **表名称：** 单据体-子表
- **表名：** t_qcqs_rptkeyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frptid | 报表实体 | varchar | 255 |  | √ | '0' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcqs_rptkry_fid |  | fid |
| 2 | idx_qcqs_rptkry_fseq |  | fseq |
| 3 | pk_qcqs_rptkeyentry |  | fentryid |

---

## 统计分析报表关键字-多语言表 t_qcqs_analyrptkey_l

- **表名称：** 统计分析报表关键字-多语言表
- **表名：** t_qcqs_analyrptkey_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 关键字名称 | varchar | 150 |  | √ | ' ' | 关键字名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcqs_analeyl_fname |  | fname |
| 2 | pk_qcqs_analyrptkey_l |  | fpkid |
| 3 | idx_qcqs_analeyl_fid |  | fid,flocaleid |
