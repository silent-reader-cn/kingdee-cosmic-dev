# 资产盘点表-fa_inventory_record_group

## 资产盘点表-关联追踪表 t_fa_inventory_group_tc

- **表名称：** 资产盘点表-关联追踪表
- **表名：** t_fa_inventory_group_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_inventory_group_tc_tbill |  | ftbillid |
| 2 | idx_fa_inventory_group_tc_tid |  | ftid |
| 3 | pk_fa_inventory_group_tc |  | fid |
| 4 | idx_fa_inventory_gp_tc_tbill |  | ftbillid |

---

## 单据体-子表 t_fa_inventory_record

- **表名称：** 单据体-子表
- **表名：** t_fa_inventory_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdifference | 差异数量 | numeric | 23 | 10 | √ | 0.0000000000 | 差异数量 |
| 3 | finventoryuser | 盘点人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmodel | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 5 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 6 | finventorytime | 盘点日期 | timestamp | 0 |  |  | null | 盘点日期 |
| 7 | finventoryquantity | 盘点数量 | numeric | 23 | 10 | √ | 0.0000000000 | 盘点数量 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fgroupnumber | fgroupnumber | varchar | 30 |  | √ | ' ' |  |
| 10 | fbillstate | fbillstate | bpchar | 1 |  | √ | '0' |  |
| 11 | fheaduserid | 使用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fbarcode | 条形码 | varchar | 60 |  | √ | ' ' | 条形码 |
| 14 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | 存放地点 fa_storeplace |
| 15 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 16 | fheadusedeptid | 使用部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | finventoryway | 盘点方式 | bpchar | 1 |  | √ | ' ' | 盘点方式,枚举: A :人人盘点 B :手工盘点 C :API导入 D :人人PC盘点 E :扫码盘点 |
| 18 | finventorystate | 盘点状态 | bpchar | 1 |  | √ | 'B' | 盘点状态,枚举: A :已盘 B :未盘 C :已生成差异 |
| 19 | fbillno | fbillno | varchar | 60 |  | √ | ' ' |  |
| 20 | fbookquantity | 账存数量 | numeric | 23 | 10 | √ | 0.0000000000 | 账存数量 |
| 21 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 22 | fname | 资产名称 | varchar | 100 |  | √ | ' ' | 资产名称 |
| 23 | finventorytaskid | finventorytaskid | int8 | 64 |  | √ | 0 |  |
| 24 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | 'C' |  |
| 25 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 26 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 28 | freason | 盘点说明 | varchar | 100 |  | √ | ' ' | 盘点说明 |
| 29 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 30 | finventschemeentryid | finventschemeentryid | int8 | 64 |  | √ | 0 |  |
| 31 | fnumber | 资产编码 | varchar | 80 |  | √ | ' ' | 资产编码 |
| 32 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_inventory_record_pkey |  | fid |
| 2 | idx_fa_inventory_record |  | finventschemeentryid,finventorytaskid |
| 3 | idx_fa_inventory_red_fgid |  | fgroupid |

---

## 资产盘点表-反写记录表 t_fa_inventory_group_wb

- **表名称：** 资产盘点表-反写记录表
- **表名：** t_fa_inventory_group_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_inventory_group_wb |  | fentryid |
| 2 | idx_fa_inventory_group_wb_fk |  | fid |

---

## 关联子实体-子表 t_fa_inventory_group_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_inventory_group_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_inventory_group_lk_fk |  | fgroupid |
| 2 | pk_fa_inventory_group_lk |  | fpkid |

---

## 资产盘点表-主表 t_fa_inventory_group

- **表名称：** 资产盘点表-主表
- **表名：** t_fa_inventory_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fschemeid | 盘点方案 | int8 | 64 |  | √ | 0 | 盘点方案 fa_inventscheme_new |
| 7 | fassetunit | 资产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fgroupid | fgroupid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_inventory_group |  | fgroupid |
| 2 | idx_inventory_group_billno |  | fbillno |

---

## 资产盘点表-多语言表 t_fa_inventory_group_l

- **表名称：** 资产盘点表-多语言表
- **表名：** t_fa_inventory_group_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_inventory_group_l |  | fpkid |
| 2 | idx_inventory_group_l_lcid |  | fgroupid,flocaleid |
