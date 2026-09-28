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
| 3 | finventoryuser | 盘点人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmodel | 规格型号 | varchar | 255 |  | √ | ' ' | 规格型号 |
| 5 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 6 | fismanual | 是否手动确认盘点 | bpchar | 1 |  | √ | '0' | 是否手动确认盘点 |
| 7 | finventorytime | 盘点日期 | timestamp | 0 |  |  | null | 盘点日期 |
| 8 | finventoryquantity | 盘点数量 | numeric | 23 | 10 | √ | 0.0000000000 | 盘点数量 |
| 9 | ficheadusepersonid | 盘点变动使用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fgroupnumber | fgroupnumber | varchar | 30 |  | √ | ' ' |  |
| 12 | fbillstate | fbillstate | bpchar | 1 |  | √ | '0' |  |
| 13 | fheaduserid | 使用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 15 | fbarcode | 条形码 | varchar | 60 |  | √ | ' ' | 条形码 |
| 16 | ficstoreplaceid | 盘点变动存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 17 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 18 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 19 | fheadusedeptid | 使用部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | finventoryway | 盘点方式 | bpchar | 1 |  | √ | ' ' | 盘点方式,枚举: B :手工盘点 C :API导入 D :个人自盘（PC端） E :PDA扫码盘点 F :PDA手工盘点 G :个人扫码自盘（移动端） H :个人手工自盘（移动端） |
| 21 | finventorystate | 盘点状态 | bpchar | 1 |  | √ | 'B' | 盘点状态,枚举: A :已盘 B :未盘 C :已生成差异 |
| 22 | fchangebillid | 变更单id | int8 | 64 |  | √ | 0 | 变更单id |
| 23 | fisnewadd | 是否手工新增行 | bpchar | 1 |  | √ | '0' | 是否手工新增行 |
| 24 | fisconfirm | 确认盘点完成 | bpchar | 1 |  | √ | '0' | 确认盘点完成 |
| 25 | fbillno | fbillno | varchar | 60 |  | √ | ' ' |  |
| 26 | fbookquantity | 账存数量 | numeric | 23 | 10 | √ | 0.0000000000 | 账存数量 |
| 27 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 28 | fname | 资产名称 | varchar | 100 |  | √ | ' ' | 资产名称 |
| 29 | finventorytaskid | finventorytaskid | int8 | 64 |  | √ | 0 |  |
| 30 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | 'C' |  |
| 31 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 32 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | fadheadusedeptid | 账存使用部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | finvresult | 盘点结果 | varchar | 50 |  | √ | ' ' | 盘点结果,枚举: 1 :盘亏 2 :盘盈 3 :不符 4 :账实相符 |
| 35 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 36 | freason | 盘点说明 | varchar | 100 |  | √ | ' ' | 盘点说明 |
| 37 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 38 | fadstoreplaceid | 账存存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 39 | ficheadusedeptid | 盘点变动使用部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | finventschemeentryid | finventschemeentryid | int8 | 64 |  | √ | 0 |  |
| 41 | finvdifferid | 盘亏盘盈单id | int8 | 64 |  | √ | 0 | 盘亏盘盈单id |
| 42 | fnumber | 资产编码 | varchar | 80 |  | √ | ' ' | 资产编码 |
| 43 | fadheadusepersonid | 账存使用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

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
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | finventorymode | 盘点模式 | varchar | 200 |  | √ | ' ' | 盘点模式,枚举: |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fschemeid | 盘点方案 | int8 | 64 |  | √ | 0 | [盘点方案 fa_inventscheme_new](../fa_files/fa_inventscheme_new.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmigsrc | 是否迁移 | int4 | 32 |  | √ | 0 | 是否迁移 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | finventorypersonid | 盘点负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fassetunit | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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
