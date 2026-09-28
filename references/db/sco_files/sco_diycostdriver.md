# 自定义费用分配标准值维护-sco_diycostdriver

## 自定义费用分配标准值维护-多语言表 t_sco_diycostdriver_l

- **表名称：** 自定义费用分配标准值维护-多语言表
- **表名：** t_sco_diycostdriver_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_diycostdriver_l |  | fpkid |
| 2 | idx_sco_diycostdriver_l |  | flocaleid,fremark |

---

## 单据体-子表 t_sco_diycostdriverentry

- **表名称：** 单据体-子表
- **表名：** t_sco_diycostdriverentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fmaterialgroupid | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmatauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 8 | fmatnumid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | fmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 10 | fentryqty | 数值 | numeric | 23 | 10 | √ | 0 | 数值 |
| 11 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 12 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | [成本核算对象f7 sco_costobjectf7](../sco_files/sco_costobjectf7.md) |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fbenefcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_diycostdriverentry |  | fentryid |
| 2 | idx_sco_diycostdriverentry |  | fbenefcostcenterid,fcostobjectid |
| 3 | idx_sco_diycostdriverentry2 |  | fid |

---

## 自定义费用分配标准值维护-主表 t_sco_diycostdriver

- **表名称：** 自定义费用分配标准值维护-主表
- **表名：** t_sco_diycostdriver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 核算组织(20240613版本多核算体系废弃) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsourceid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 5 | feffectstatus | 生效状态 | varchar | 30 |  | √ | ' ' | 生效状态,枚举: A :未生效 E :已生效 F :已失效 |
| 6 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 7 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sco :标准成本 |
| 8 | fcostbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsourcetype | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: SYS :按配置方案导入 NEW :手工新增 |
| 13 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 14 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 15 | fcostdriverid | 费用分配标准 | int8 | 64 |  | √ | 0 | [费用分配标准 sco_costdriver](../sco_files/sco_costdriver.md) |
| 16 | fqty | 数值 | numeric | 23 | 10 | √ | 0 | 数值 |
| 17 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 18 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fexpperiodid | 失效期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 24 | fmaterialgroupstdid | 物料分类标准 | int8 | 64 |  | √ | 0 | [物料分类标准 bd_materialgroupstandard](../basedata_files/bd_materialgroupstandard.md) |
| 25 | fcollconfigid | 配置单 | int8 | 64 |  | √ | 0 | [成本归集配置单 sco_costcollectconfig](../sco_files/sco_costcollectconfig.md) |
| 26 | feffectperiodid | 生效期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 27 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sco_diycostdriver |  | fid |
| 2 | idx_sco_diycostdriver |  | forgid,fcostcenterid,fcostdriverid |
