# 土地增值税预缴共享方案-tcret_tdzzs_edit_share

## 适用房产类型子目-子表 t_tcret_tdzzs_sharefclxzm

- **表名称：** 适用房产类型子目-子表
- **表名：** t_tcret_tdzzs_sharefclxzm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | ffclxzmid | 房产类型子目 | int8 | 64 |  | √ | 0 | [房产类型子目 tcret_tdzzs_fclxzm](../tcret_files/tcret_tdzzs_fclxzm.md) |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_tdzzs_sharefclxzm_fk |  | fentryid |
| 2 | pk_tcret_tdzzs_sharefclxzm |  | fdetailid |

---

## 规则-子表 t_tcret_tdzzs_sharerule

- **表名称：** 规则-子表
- **表名：** t_tcret_tdzzs_sharerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: yjrule :预缴申报项规则 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_tdzzs_sharerule |  | fdetailid |
| 2 | idx_tcret_tdzzs_sharerule_fk |  | fentryid |

---

## 土地增值税预缴共享方案-主表 t_tcret_tdzzs_edit_share

- **表名称：** 土地增值税预缴共享方案-主表
- **表名：** t_tcret_tdzzs_edit_share

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fautoshar | 自动共享 | bpchar | 1 |  | √ | '0' | 自动共享 |
| 4 | fplanname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_tdzzs_edit_share |  | fid |
| 2 | idx_t_tcret_tdzzseditshare |  | forgid |

---

## 适用预缴项目-子表 t_tcret_tdzzs_shareyjxm

- **表名称：** 适用预缴项目-子表
- **表名：** t_tcret_tdzzs_shareyjxm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fprepayid | 预缴项目 | int8 | 64 |  | √ | 0 | [土地增值税项目 tdm_tdzzs_clearing_unit](../tdm_files/tdm_tdzzs_clearing_unit.md) |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_tdzzs_shareyjxm |  | fdetailid |
| 2 | idx_tcret_tdzzs_shareyjxm_fk |  | fentryid |

---

## 被共享组织-子表 t_tcret_tdzzs_shareorg

- **表名称：** 被共享组织-子表
- **表名：** t_tcret_tdzzs_shareorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_tdzzs_shareorg_fk |  | fentryid |
| 2 | pk_tcret_tdzzs_shareorg |  | fdetailid |

---

## 共享方案-子表 t_tcret_tdzzs_share

- **表名称：** 共享方案-子表
- **表名：** t_tcret_tdzzs_share

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 8 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 9 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 10 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 11 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fbasedatapropfield | fbasedatapropfield | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcret_tdzzs_share_fk |  | fid |
| 2 | pk_tcret_tdzzs_share |  | fentryid |

---

## 共享方案-多语言表 t_tcret_tdzzs_share_l

- **表名称：** 共享方案-多语言表
- **表名：** t_tcret_tdzzs_share_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 共享方案名 | varchar | 50 |  | √ | ' ' | 共享方案名 |
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
| 1 | pk_tcret_tdzzs_share_l |  | fpkid |
| 2 | idx_tcret_tdzzs_share_l_0 |  | fentryid,flocaleid |
