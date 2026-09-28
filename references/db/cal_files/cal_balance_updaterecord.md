# 存货成本日志-cal_balance_updaterecord

## 存货成本日志-主表 t_cal_balancerecord

- **表名称：** 存货成本日志-主表
- **表名：** t_cal_balancerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 4 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 5 | finorout | 收发方向 | varchar | 80 |  | √ | 'IN' | 收发方向,枚举: IN :收入 OUT :发出 |
| 6 | fsource | 更新来源 | bpchar | 1 |  | √ | 'A' | 更新来源,枚举: A :成本记录创建 B :即时成本 C :费用暂估 D :费用分摊 E :入库成本维护 W :出库成本维护 F :入库成本汇总维护 Y :出库成本汇总维护 G :出库核算 H :成本调整单审核 I :成本记录删除 J :成本调整单反审核 K :勾稽 Z :反勾稽 M :取消暂估 N :取消分摊 O :实际成本核算 P :返工取价 Q :其他存货核算 R :标准成本差异单审核 S :标准成本差异单反审核 T :零成本批量维护 U :应付结算清单 V :委外入库成本维护 |
| 7 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 8 | fdevcost | 研发费用 | varchar | 10 |  | √ | '0' | 研发费用,枚举: 1 :是 0 :否 |
| 9 | factualcost | 更新成本 | numeric | 23 | 10 | √ | 0.0000000000 | 更新成本 |
| 10 | fassistid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 12 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 13 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 14 | flot | 批号 | varchar | 255 |  | √ | ' ' | 批号 |
| 15 | fbillno | 单据编码 | varchar | 80 |  | √ | ' ' | 单据编码 |
| 16 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 18 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 19 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 20 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 21 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 23 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 25 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 26 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 27 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 28 | fbillentityid | 单据对象 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 29 | fbaseqty | 更新数量 | numeric | 23 | 10 | √ | 0.0000000000 | 更新数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_balancerecord_pkey |  | fid |
| 2 | idx_cal_balancercd_mw |  | fmaterialid,fwarehouseid |
| 3 | idx_cal_balancercd_ownerid |  | fownerid |
| 4 | idx_cal_balancercd_cmp |  | fcostaccountid,fmaterialid,fperiodid,fstorageorgunitid,fwarehouseid |
| 5 | idx_cal_balrecord_fupdtime |  | fupdatetime |
| 6 | idx_cal_balancercd_projectid |  | fprojectid |
| 7 | idx_cal_balancercd_wh |  | fwarehouseid |
| 8 | idx_cal_balancerecord_fbillno |  | fbillno |

---

## 单据体-子表 t_cal_balancerecordentry

- **表名称：** 单据体-子表
- **表名：** t_cal_balancerecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcostsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fsubactualcost | 子要素更新成本 | numeric | 23 | 10 | √ | 0.0000000000 | 子要素更新成本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_balancerecordentry_fid |  | fid |
| 2 | t_cal_balancerecordentry_pkey |  | fentryid |
