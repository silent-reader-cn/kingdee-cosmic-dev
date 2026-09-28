# 操作校验方案-msbd_dmfvalidscheme

## 操作校验单元清单-子表 t_msbd_dmfvschemeentry

- **表名称：** 操作校验单元清单-子表
- **表名：** t_msbd_dmfvschemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdmfunitenable | fdmfunitenable | bpchar | 1 |  | √ | '0' |  |
| 3 | fdmfunitid | fdmfunitid | int8 | 64 |  | √ | 0 |  |
| 4 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msbd_dmfvschemeentry |  | fentryid |
| 2 | idx_msbd_dmfvschemeentry |  | fid |

---

## 操作校验方案-多语言表 t_msbd_dmfvscheme_l

- **表名称：** 操作校验方案-多语言表
- **表名：** t_msbd_dmfvscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' |  |
| 4 | fdescription | fdescription | varchar | 512 |  |  | null |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msbd_dmfvscheme_l |  | fpkid |
| 2 | idx_msbd_dmfvscheme_l_fname |  | fname,fid |
| 3 | idx_msbd_dmfvscheme_l_fid |  | fid,flocaleid |

---

## 操作校验方案-主表 t_msbd_dmfvscheme

- **表名称：** 操作校验方案-主表
- **表名：** t_msbd_dmfvscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | fregstatus | fregstatus | varchar | 5 |  | √ | ' ' |  |
| 5 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 6 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 7 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 8 | fdescription | fdescription | varchar | 512 |  |  | null |  |
| 9 | fispreset | fispreset | bpchar | 1 |  | √ | '0' |  |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fstatus | fstatus | varchar | 5 |  | √ | ' ' |  |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 14 | fentityoperation | fentityoperation | varchar | 50 |  | √ | ' ' |  |
| 15 | fenable | fenable | varchar | 5 |  | √ | ' ' |  |
| 16 | fnumber | fnumber | varchar | 80 |  | √ | ' ' |  |
| 17 | fentityid | fentityid | varchar | 36 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msbd_dmfvscheme |  | fid |
| 2 | idx_msbd_dmfvscheme_fnumber |  | fnumber |
