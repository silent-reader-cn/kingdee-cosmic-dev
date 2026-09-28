# 物料销售信息-bd_materialsalinfo

## 物料销售信息-使用范围表 t_bd_materialsalinfo_u

- **表名称：** 物料销售信息-使用范围表
- **表名：** t_bd_materialsalinfo_u

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
| 1 | t_bd_materialsalinfo_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_bd_materialsalinfo_u_uo |  | fuseorgid |

---

## 物料销售信息-使用范围位图表 t_bd_materialsalinfo_m

- **表名称：** 物料销售信息-使用范围位图表
- **表名：** t_bd_materialsalinfo_m

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
| 1 | pk_t_bd_materialsalinfo_m |  | forgid |

---

## 物料销售信息-多语言表 t_bd_materialsalinfo_l

- **表名称：** 物料销售信息-多语言表
- **表名：** t_bd_materialsalinfo_l

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
| 1 | idx_materialsalinfo_l_fid |  | flocaleid,fid |
| 2 | t_bd_materialsalinfo_l_pkey |  | fpkid |

---

## 物料销售信息-主表 t_bd_materialsalinfo

- **表名称：** 物料销售信息-主表
- **表名：** t_bd_materialsalinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 销售分类 | int8 | 64 |  | √ | 0 | [销售分类 bd_materialsalgroup](../sbd_files/bd_materialsalgroup.md) |
| 3 | fdlivrateceiling | 发货超发比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 发货超发比率(%) |
| 4 | fdeliveradvdays | 发货提前天数 | int8 | 64 |  | √ | 0 | 发货提前天数 |
| 5 | fiscontrolqty | 控制发货数量 | bpchar | 1 |  | √ | '0' | 控制发货数量 |
| 6 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsuiteinnersettletype | 套件内部结算方式 | varchar | 50 |  | √ | ' ' | 套件内部结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsuitestructctrl | 套件结构控制 | varchar | 50 |  | √ | ' ' | 套件结构控制,枚举: unadj :不可调整 adj :可调整 |
| 12 | fminorderqty | 起销量 | numeric | 23 | 10 | √ | 0.0000000000 | 起销量 |
| 13 | fsalesvalunitid | 销售计价单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fisreturn | 允许退货(封存) | bpchar | 1 |  | √ | '0' | 允许退货(封存) |
| 16 | fdlivratefloor | 发货欠发比率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 发货欠发比率(%) |
| 17 | fqcorgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fcontrolunit | 超发控制单位 | varchar | 5 |  | √ | ' ' | 超发控制单位,枚举: SU :销售单位 IU :库存单位 |
| 19 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 20 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fmbdmasterid | 物料销售信息内码 | int8 | 64 |  | √ | 0 | 物料销售信息内码 |
| 22 | fcommoninfoid | 物料组织公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 23 | fispartialreturn | 部件可退(封存) | bpchar | 1 |  | √ | '0' | 部件可退(封存) |
| 24 | fwarrantyperiod | 保修期 | numeric | 23 | 10 | √ | 0.0000000000 | 保修期 |
| 25 | fenable | 销售信息使用状态 | varchar | 5 |  | √ | ' ' | 销售信息使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fsuitesettletype | 套件结算方式 | varchar | 50 |  | √ | ' ' | 套件结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 27 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 28 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fwarrantyunit | 保修期单位 | varchar | 5 |  | √ | ' ' | 保修期单位,枚举: M :月 D :日 Y :年 |
| 31 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 32 | fdeliverdelaydays | 发货延迟天数 | int8 | 64 |  | √ | 0 | 发货延迟天数 |
| 33 | fstatus | 销售信息数据状态 | varchar | 5 |  | √ | ' ' | 销售信息数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fmasterid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 36 | fbondcontrol | 保税控制 | bpchar | 1 |  | √ | '0' | 保税控制,枚举: 0 :非保税 1 :保税 2 :不控制 |
| 37 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 38 | fisstockinbaseqc | 退货根据检验结果入库 | bpchar | 1 |  | √ | '0' | 退货根据检验结果入库 |
| 39 | fcreateorgid | 销售信息创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fisreturnneedntqc | 销售退换免检 | bpchar | 1 |  | √ | '0' | 销售退换免检 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fiscontrolday | 控制时间 | bpchar | 1 |  | √ | '0' | 控制时间 |
| 43 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 44 | fsalesunitid | 销售单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 45 | fisqcbfdeliver | 发货检验 | bpchar | 1 |  | √ | '0' | 发货检验 |
| 46 | fiswarranty | 保修 | bpchar | 1 |  | √ | '0' | 保修 |
| 47 | fctrlstrategy | 销售信息控制策略 | varchar | 5 |  | √ | ' ' | 销售信息控制策略,枚举: 2 :分配/局部共享 7 :私有 5 :全局共享 |
| 48 | fisautonew | 自动新增 | bpchar | 1 |  | √ | '0' | 自动新增 |
| 49 | fsuitereturntype | 套件退货方式 | varchar | 50 |  | √ | ' ' | 套件退货方式,枚举: kitreturn :成套退货 nonkitreturn :非成套退货 |
| 50 | fsuitedeliverytype | 套件发货方式 | varchar | 50 |  | √ | ' ' | 套件发货方式,枚举: kitdeliver :成套发货 nonkitdeliver :非成套发货 |
| 51 | fisatpcheck | ATP检查 | bpchar | 1 |  | √ | '0' | ATP检查 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_materialsalinfo_master |  | fmasterid |
| 2 | idx_t_bd_materialsalinfo_createorg |  | fcreateorgid |
| 3 | idx_bd_matsale_ctrlstrategy |  | fctrlstrategy |
| 4 | idx_bd_matsalinfo_fmatid |  | fmasterid |
| 5 | idx_t_bd_materialsalinfosrcid |  | fsourcedataid |
| 6 | t_bd_materialsalinfo_pkey |  | fid |
| 7 | idx_t_bd_materialsalinfobit |  | fbitindex |
