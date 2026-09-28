# 扫描录入字段-barcm_scaneditfield

## 扫描录入字段-主表 t_barcm_scaneditfield

- **表名称：** 扫描录入字段-主表
- **表名：** t_barcm_scaneditfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fispreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ffieldkey | 字段标识 | varchar | 80 |  | √ | ' ' | 字段标识 |
| 10 | ffieldseq | 字段序号 | int8 | 64 |  | √ | 0 | 字段序号 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_barcm_sefield_number |  | fnumber |
| 2 | pk_barcm_scaneditfield |  | fid |

---

## 扫描录入字段-多语言表 t_barcm_scaneditfield_l

- **表名称：** 扫描录入字段-多语言表
- **表名：** t_barcm_scaneditfield_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_barcm_scaneditfield_l |  | fpkid |
| 2 | idx_barcm_sefield_fidflid |  | fid,flocaleid |
