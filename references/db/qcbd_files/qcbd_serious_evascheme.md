# 严重程度评估方案-qcbd_serious_evascheme

## 严重性单据体-子表 t_qcnd_seriousentry

- **表名称：** 严重性单据体-子表
- **表名：** t_qcnd_seriousentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fseriouslevel | 严重性等级 | numeric | 23 | 10 | √ | 0 | 严重性等级 |
| 5 | fjudgestd | 判定标准 | varchar | 255 |  | √ | ' ' | 判定标准 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcnd_seriry_fid |  | fid |
| 2 | idx_qcnd_seriry_fseq |  | fseq |
| 3 | pk_qcnd_seriousentry |  | fentryid |

---

## 发生频率单据体-子表 t_qcbd_happenrateentry

- **表名称：** 发生频率单据体-子表
- **表名：** t_qcbd_happenrateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhappenratelevel | 发生频率等级 | numeric | 23 | 10 | √ | 0 | 发生频率等级 |
| 3 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fjudgestd | 判定标准 | varchar | 255 |  | √ | ' ' | 判定标准 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_happry_fid |  | fid |
| 2 | idx_qcbd_happry_fseq |  | fseq |
| 3 | pk_qcbd_happenrateentry |  | fentryid |

---

## 严重程度评估方案-使用范围表 t_qcbd_serlevelscheme_u

- **表名称：** 严重程度评估方案-使用范围表
- **表名：** t_qcbd_serlevelscheme_u

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
| 1 | pk_t_qcbd_serlevelscheme_u |  | fdataid,fuseorgid |
| 2 | idx_t_qcbd_serlevelscheme_u_uo |  | fuseorgid |

---

## 严重程度评估方案-多语言表 t_qcbd_serlevelscheme_l

- **表名称：** 严重程度评估方案-多语言表
- **表名：** t_qcbd_serlevelscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | fcomment | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_serlmel_fname |  | fname |
| 2 | pk_qcbd_serlevelscheme_l |  | fpkid |
| 3 | idx_qcbd_serlmel_fid |  | fid,flocaleid |

---

## 严重程度评估方案-使用范围位图表 t_qcbd_serlevelscheme_m

- **表名称：** 严重程度评估方案-使用范围位图表
- **表名：** t_qcbd_serlevelscheme_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcbd_serlevelscheme_m |  | forgid |

---

## 探测度单据体-子表 t_qcbd_searchdeepentry

- **表名称：** 探测度单据体-子表
- **表名：** t_qcbd_searchdeepentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsearchdeeplevel | 探测度等级 | numeric | 23 | 10 | √ | 0 | 探测度等级 |
| 3 | fdescribe | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fjudgestd | 判定标准 | varchar | 255 |  | √ | ' ' | 判定标准 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcbd_searchdeepentry |  | fentryid |
| 2 | idx_qcbd_searry_fseq |  | fseq |
| 3 | idx_qcbd_searry_fid |  | fid |

---

## 严重程度评估方案-主表 t_qcbd_serlevelscheme

- **表名称：** 严重程度评估方案-主表
- **表名：** t_qcbd_serlevelscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsearchdeepmax | 探测度最大值 | numeric | 23 | 10 | √ | 0 | 探测度最大值 |
| 4 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fhappenratemax | 发生频率最大值 | numeric | 23 | 10 | √ | 0 | 发生频率最大值 |
| 7 | fcomment | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fseriousmax | 严重性最大值 | numeric | 23 | 10 | √ | 0 | 严重性最大值 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 15 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fseriouslevelmax | 严重程度最大值 | numeric | 23 | 10 | √ | 0 | 严重程度最大值 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 20 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 21 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_serlme_fnumber |  | fnumber |
| 2 | idx_t_qcbd_serlevelscheme_createorg |  | fcreateorgid |
| 3 | pk_qcbd_serlevelscheme |  | fid |
| 4 | idx_qcbd_serlme_fcreatetime |  | fcreatetime |
| 5 | idx_t_qcbd_serlevelscheme_master |  | fmasterid |

---

## 评估方案单据体-子表 t_qcbd_eavscheme

- **表名称：** 评估方案单据体-子表
- **表名：** t_qcbd_eavscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevelstart | 起始值 | numeric | 23 | 10 | √ | 0 | 起始值 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fseriouslevelid | 严重程度等级 | int8 | 64 |  | √ | 0 | [严重程度等级 qcbd_seriouslevel](../qcbd_files/qcbd_seriouslevel.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fimprovewayid | 改善对策 | int8 | 64 |  | √ | 0 | [改善对策 qcbd_improveway](../qcbd_files/qcbd_improveway.md) |
| 7 | flevelend | 截止值（含） | numeric | 23 | 10 | √ | 0 | 截止值（含） |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcbd_eavsme_fid |  | fid |
| 2 | pk_qcbd_eavscheme |  | fentryid |
| 3 | idx_qcbd_eavsme_fseq |  | fseq |
