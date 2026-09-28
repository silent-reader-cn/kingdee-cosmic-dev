# 盘点表-im_invcountbill

## 盘点表-关联追踪表 t_im_invcountbill_tc

- **表名称：** 盘点表-关联追踪表
- **表名：** t_im_invcountbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
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
| 1 | t_im_invcountbill_tc_pkey |  | fid |
| 2 | idx_im_invcountbill_tc_tid |  | ftid |
| 3 | idx_im_invcountbill_tc_tbill |  | ftbillid |
| 4 | idx_im_invcount_tc_ftbidtid |  | ftbillid,ftid |

---

## 盘点表-多语言表 t_im_invcountbill_l

- **表名称：** 盘点表-多语言表
- **表名：** t_im_invcountbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_invcountbill_l |  | fid,flocaleid |
| 2 | t_im_invcountbill_l_pkey |  | fpkid |

---

## 物料明细-子表 t_im_invcountbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_invcountbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty3rdacc | 账存辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 账存辅助数量(2) |
| 3 | fgainqty3rd | 盘盈辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 盘盈辅助数量(2) |
| 4 | fcheckqtyunit2nd | 复盘辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 复盘辅助数量 |
| 5 | fsourceflag | 来源标识 | varchar | 5 |  | √ | ' ' | 来源标识,枚举: 0 :方案原有 1 :实盘新增 |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fadjustqty | 调整数量 | numeric | 23 | 10 | √ | 0.0000000000 | 调整数量 |
| 9 | finvlossqty | finvlossqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 11 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | fadjustqty3rd | 调整辅助数量(2) | numeric | 23 | 10 | √ | 0 | 调整辅助数量(2) |
| 13 | fbaseqtyacc | 账存基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 账存基本数量 |
| 14 | fownertype | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 15 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | finvaccid | 即时库存标识位 | int8 | 64 |  | √ | 0 | 即时库存标识位 |
| 18 | fqty | 盘点数量 | numeric | 23 | 10 | √ | 0.0000000000 | 盘点数量 |
| 19 | fbasegainqty | 盘盈基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 盘盈基本数量 |
| 20 | fserialunitid | 序列号单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 23 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 25 | fcheckbaseqty | 复盘基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 复盘基本数量 |
| 26 | fkeepertype | 保管者类型 | varchar | 36 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 27 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 28 | fadjustbaseqty | 调整基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 调整基本数量 |
| 29 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 30 | flossqty3rd | 盘亏辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 盘亏辅助数量(2) |
| 31 | finvunitid | finvunitid | int8 | 64 |  | √ | 0 |  |
| 32 | fqtyunit2nd | 盘点辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 盘点辅助数量 |
| 33 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | flotid | 批号ID | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 35 | finvqtyacc | finvqtyacc | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 36 | fqtyinvunit | fqtyinvunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 37 | fadjustqtyunit2nd | 调整辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 调整辅助数量 |
| 38 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 39 | finvgainqty | finvgainqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | fmaterialname | fmaterialname | varchar | 100 |  | √ | ' ' |  |
| 42 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 43 | flossqty | 盘亏数量 | numeric | 23 | 10 | √ | 0.0000000000 | 盘亏数量 |
| 44 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 45 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 46 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 47 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 48 | fgainqty2nd | 盘盈辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 盘盈辅助数量 |
| 49 | fqty2ndacc | 账存辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 账存辅助数量 |
| 50 | fserialunitrate | 换算率(序列号) | numeric | 23 | 10 | √ | 0.0000000000 | 换算率(序列号) |
| 51 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 52 | freplay | 复盘 | bpchar | 1 |  | √ | '0' | 复盘 |
| 53 | fcheckqty | 复盘数量 | numeric | 23 | 10 | √ | 0.0000000000 | 复盘数量 |
| 54 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 55 | fbaselossqty | 盘亏基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 盘亏基本数量 |
| 56 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 57 | fseriallossqty | 序列号盘亏数量 | numeric | 23 | 10 | √ | 0.0000000000 | 序列号盘亏数量 |
| 58 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 59 | fcheckqty3rd | 复盘辅助数量(2) | numeric | 23 | 10 | √ | 0 | 复盘辅助数量(2) |
| 60 | fqtyacc | 账存数量 | numeric | 23 | 10 | √ | 0.0000000000 | 账存数量 |
| 61 | fsrcbillentity | 来源单据实体 | varchar | 100 |  | √ | ' ' | 来源单据实体 |
| 62 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 63 | finvunitrate | finvunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 64 | fgainqty | 盘盈数量 | numeric | 23 | 10 | √ | 0.0000000000 | 盘盈数量 |
| 65 | fserialgainqty | 序列号盘盈数量 | numeric | 23 | 10 | √ | 0.0000000000 | 序列号盘盈数量 |
| 66 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 67 | flossqty2nd | 盘亏辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 盘亏辅助数量 |
| 68 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 69 | fqtyunit3rd | 盘点辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 盘点辅助数量(2) |
| 70 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 71 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 72 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 73 | fbaseqty | 盘点基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 盘点基本数量 |
| 74 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_invcountbillentry_pkey |  | fentryid |
| 2 | idx_im_invcountbillentry_wh |  | fwarehouseid |
| 3 | idx_im_invcountbillentry_fid |  | fid |
| 4 | idx_im_invcountbillentry_mmt |  | fmaterialmasterid |

---

## 关联子实体-子表 t_im_invcountbillentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_invcountbillentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_invcountbillentry_lk_fk |  | fentryid |
| 2 | t_im_invcountbillentry_lk_pkey |  | fpkid |

---

## 盘点表-主表 t_im_invcountbill

- **表名称：** 盘点表-主表
- **表名：** t_im_invcountbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcounttype | 盘点方式 | varchar | 5 |  | √ | ' ' | 盘点方式,枚举: A :定期盘点 |
| 3 | fschemenumber | 盘点方案编号 | varchar | 80 |  | √ | ' ' | 盘点方案编号 |
| 4 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 5 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fschemeid | 盘点方案ID | int8 | 64 |  | √ | 0 | 盘点方案ID |
| 7 | ferrmsg_tag | 生成异常日志_详情 | text | 0 |  |  | null | 生成异常日志_详情 |
| 8 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fbackupcondition | 数据备份条件 | varchar | 30 |  | √ | 'invacc' | 数据备份条件,枚举: invacc :即时库存 enddateinvacc :截止日期库存 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | faccessnode | 取数节点 | varchar | 10 |  | √ | 'start' | 取数节点,枚举: start :截止日期初始 end :截止日期结存 |
| 13 | fdefaultvalue | 盘点数量默认值设置 | varchar | 5 |  | √ | ' ' | 盘点数量默认值设置,枚举: B :0 A :账存数量 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 19 | fchecker2ndid | 复盘人 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 22 | fcheckerid | 盘点人 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 23 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 |
| 26 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 27 | fenablecheck | 启用复盘 | bpchar | 1 |  | √ | '0' | 启用复盘 |
| 28 | fschemename | 盘点方案名称 | varchar | 80 |  | √ | ' ' | 盘点方案名称 |
| 29 | ferrmsg | 生成异常日志 | varchar | 255 |  | √ | ' ' | 生成异常日志 |
| 30 | fexcludeenddate | 排除补单 | bpchar | 1 |  | √ | '1' | 排除补单 |
| 31 | fpushstatus | 盘盈/盘亏生成状态 | varchar | 50 |  | √ | ' ' | 盘盈/盘亏生成状态,枚举: 0 :未生成 1 :生成中 2 :已生成 3 :生成失败 |
| 32 | finvaccdate | 账存日期 | timestamp | 0 |  |  | null | 账存日期 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_invcountbill_org |  | forgid |
| 2 | t_im_invcountbill_pkey |  | fid |
| 3 | idx_im_invcountbill_billno |  | fbillno |
| 4 | idx_im_invcountbill_biztorgno |  | fbiztime,forgid,fbillno |

---

## 盘点表-反写记录表 t_im_invcountbill_wb

- **表名称：** 盘点表-反写记录表
- **表名：** t_im_invcountbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_im_invcountbill_wb_pkey |  | fentryid |
| 2 | idx_im_invcountbill_wb_fk |  | fid |

---

## 关联子实体-子表 t_im_invcountbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_invcountbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_invcountbill_lk_fk |  | fid |
| 2 | t_im_invcountbill_lk_pkey |  | fpkid |
