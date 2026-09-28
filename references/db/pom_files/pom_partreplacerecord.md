# 部件更换记录-pom_partreplacerecord

## 更换部件清单-多语言表 t_pom_partrepleceentry_l

- **表名称：** 更换部件清单-多语言表
- **表名：** t_pom_partrepleceentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fpartdescription | 部件描述 | varchar | 255 |  | √ | ' ' | 部件描述 |
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
| 1 | pk_pom_partrepleceentry_l |  | fpkid |
| 2 | idx_pom_partrepleceentry_l_0 |  | fentryid,flocaleid |

---

## 更换部件清单-子表 t_pom_partrepleceentry

- **表名称：** 更换部件清单-子表
- **表名：** t_pom_partrepleceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialseq | 生产领料单对应物料及序列号 | varchar | 255 |  | √ | ' ' | 生产领料单对应物料及序列号 |
| 3 | freplemateralid | 替换下来的部件编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | frepleacedate | 更换日期 | timestamp | 0 |  |  | null | 更换日期 |
| 7 | fpartdescription | 部件描述 | varchar | 255 |  | √ | ' ' | 部件描述 |
| 8 | frepleseq | 替换下来的部件序列号 | varchar | 50 |  | √ | ' ' | 替换下来的部件序列号 |
| 9 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | freqmaterialnum | 领用的部件编码 | varchar | 80 |  | √ | ' ' | 领用的部件编码 |
| 11 | fpartlocation | 部件所属位置 | varchar | 255 |  | √ | ' ' | 部件所属位置 |
| 12 | fpromaterialentryid | fpromaterialentryid | int8 | 64 |  | √ | 0 |  |
| 13 | fuseseq | 领用的部件序列号 | varchar | 50 |  | √ | ' ' | 领用的部件序列号 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_partrepleceentry |  | fentryid |
| 2 | idx_pom_part_fmaterialseq |  | fmaterialseq |
| 3 | idx_pom_partrepleceentry_fk |  | fid |

---

## 部件更换记录-反写记录表 t_pom_partreplacerecord_wb

- **表名称：** 部件更换记录-反写记录表
- **表名：** t_pom_partreplacerecord_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_partreplacerecord_wb_fk |  | fid |
| 2 | pk_pom_partreplacerecord_wb |  | fentryid |

---

## 部件更换记录-关联追踪表 t_pom_partreplacerecord_tc

- **表名称：** 部件更换记录-关联追踪表
- **表名：** t_pom_partreplacerecord_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_partreplacerecord_tc |  | fid |
| 2 | idx_pom_partreplacerecord_tc_tbill |  | ftbillid |
| 3 | idx_pom_partreplacerecord_tc_tid |  | ftid |

---

## 关联子实体-子表 t_pom_partreplacerecord_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_partreplacerecord_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_partreplacerecord_lk |  | fpkid |
| 2 | idx_pom_partreplacerecord_lk_fk |  | fid |

---

## 部件更换记录-主表 t_pom_partreplacerecord

- **表名称：** 部件更换记录-主表
- **表名：** t_pom_partreplacerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fmaterialid | 检修设备注册号 | int8 | 64 |  | √ | 0 | [物料检修信息 mpdm_materialmtcinfo](../mpdm_files/mpdm_materialmtcinfo.md) |
| 8 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | forderno | 检修工单号 | varchar | 50 |  | √ | ' ' | 检修工单号 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pom_part_fbillno_idx |  | fbillno |
| 2 | pk_pom_partreplacerecord |  | fid |
