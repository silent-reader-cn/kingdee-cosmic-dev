# 物料成本信息-cad_matcostinfo

## 物料成本信息-多语言表 t_bd_matcostinfo_l

- **表名称：** 物料成本信息-多语言表
- **表名：** t_bd_matcostinfo_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_matcostinfo_l |  | fpkid |
| 2 | ix_bd_matcost_l_id |  | flocaleid,fid |

---

## 单据体-子表 t_bd_matcostinfoentry

- **表名称：** 单据体-子表
- **表名：** t_bd_matcostinfoentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fstandardcost | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 6 | fstepamt | 本阶金额 | numeric | 23 | 10 | √ | 0.0000000000 | 本阶金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_matcostinfoentry |  | fentryid |
| 2 | ix_bd_matcten_fsubeletid |  | fid,felementid,fsubelementid |

---

## 物料成本信息-主表 t_bd_matcostinfo

- **表名称：** 物料成本信息-主表
- **表名：** t_bd_matcostinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprocessrouteid | 工艺路线 | int8 | 64 |  | √ | 0 | [分组基础资料带组织模板 cad_router](../basedata_files/cad_router.md) |
| 3 | fbomtypeid | BOM类型 | int8 | 64 |  | √ | 0 | [BOM类型 mpdm_bomtype](../mpdm_files/mpdm_bomtype.md) |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 8 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 9 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fsource | 来源类型 | varchar | 30 |  | √ | ' ' | 来源类型,枚举: 0 :手工新增 1 :成本更新 |
| 11 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmatversionid | 物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 15 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [分组基础资料带组织模板 cad_costbom](../basedata_files/cad_costbom.md) |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fiscited | 是否被引用 | bpchar | 1 |  | √ | '0' | 是否被引用 |
| 19 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 20 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | [卷算维度数据表 cad_keycol](../cad_files/cad_keycol.md) |
| 21 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 22 | fconsidersubmaterialloss | 考虑子物料损耗 | bpchar | 1 |  | √ | '0' | 考虑子物料损耗 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fconsidervalidperiod | 考虑子物料有效期 | bpchar | 1 |  | √ | '0' | 考虑子物料有效期 |
| 25 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fiscalccurlevel | 只计算本层物料 | bpchar | 1 |  | √ | '0' | 只计算本层物料 |
| 29 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 30 | fconsiderpreparetime | 考虑准备工时 | bpchar | 1 |  | √ | '0' | 考虑准备工时 |
| 31 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: manualinput :手工录入 stdcostcalculate :系统卷算 synupdate :同步更新 manual :手工新增 contract :采购合同 order :采购订单 |
| 33 | fconsideryieldrate | 考虑成品率 | bpchar | 1 |  | √ | '0' | 考虑成品率 |
| 34 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fkeycol | 维度字段 | varchar | 255 |  | √ | ' ' | 维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_matcostinfo_id |  | fmaterialid,fcosttypeid |
| 2 | pk_t_bd_matcostinfo |  | fid |
| 3 | ix_bd_matcostinfo_keycol |  | fcosttypeid,fkeycol |
