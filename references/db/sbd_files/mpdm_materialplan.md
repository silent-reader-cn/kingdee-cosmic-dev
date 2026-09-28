# 物料计划信息-mpdm_materialplan

## 物料计划信息-分表 t_bd_materialplan_e

- **表名称：** 物料计划信息-分表
- **表名：** t_bd_materialplan_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanmode | 计划方式 | varchar | 30 |  | √ | ' ' | 计划方式,枚举: B :人工订货 C :MPS D :MRP |
| 3 | fmaterialid | fmaterialid | int8 | 64 |  | √ | 0 |  |
| 4 | fwastagerateformula | 损耗计算公式 | varchar | 30 |  | √ | ' ' | 损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） |
| 5 | finspectionleadtime | finspectionleadtime | int4 | 32 |  | √ | 0 |  |
| 6 | fdemandmergerule | 需求合并规则 | int8 | 64 |  | √ | 0 | [合并规则 mpdm_mergerule](../mpdm_files/mpdm_mergerule.md) |
| 7 | ffixedperiod | 固定周期(天) | numeric | 23 | 10 | √ | 0 | 固定周期(天) |
| 8 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fyield | 成品率% | numeric | 23 | 10 | √ | 0 | 成品率% |
| 10 | fplantimebound | 计划时界 | int4 | 32 |  | √ | 0 | 计划时界 |
| 11 | fseparatorsymbol | 分割符号 | varchar | 30 |  | √ | ' ' | 分割符号,枚举: A :+ B :- |
| 12 | freorderpoint | 再订货点 | numeric | 23 | 10 | √ | 0 | 再订货点 |
| 13 | fmaxlotsize | 最大订货量 | numeric | 23 | 10 | √ | 0 | 最大订货量 |
| 14 | fmanufacturegroupid | 制造策略组(已废弃) | int8 | 64 |  | √ | 0 | [制造策略组 mpdm_manustrategy_group](../mpdm_files/mpdm_manustrategy_group.md) |
| 15 | fpartitionbase | 分割基数 | numeric | 23 | 10 | √ | 0 | 分割基数 |
| 16 | flotpolicy | 批量政策 | varchar | 30 |  | √ | ' ' | 批量政策,枚举: A :直接批量 B :固定批量 C :周期批量 |
| 17 | fenableuserid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fwastagerate | 损耗率% | numeric | 23 | 10 | √ | 0 | 损耗率% |
| 19 | ffixedleadtime | ffixedleadtime | int4 | 32 |  | √ | 0 |  |
| 20 | forderprogressgroup | 订单进度分组 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 21 | fputinchoice | fputinchoice | varchar | 30 |  | √ | ' ' |  |
| 22 | fchangeleadtime | fchangeleadtime | int4 | 32 |  | √ | 0 |  |
| 23 | fmanufacture | 制造策略 | int8 | 64 |  | √ | 0 | [制造策略 mpdm_manustrategy](../mpdm_files/mpdm_manustrategy.md) |
| 24 | ftransportmode | 运输方式 | bpchar | 1 |  | √ | '0' | 运输方式,枚举: 0 :空 1 :公路 2 :铁路 3 :海运 4 :空运 |
| 25 | fleadtimetype | fleadtimetype | varchar | 30 |  | √ | ' ' |  |
| 26 | fbackwardperiod | 向后冲销期间(天) | int4 | 32 |  | √ | 0 | 向后冲销期间(天) |
| 27 | fintegermultiple | fintegermultiple | numeric | 23 | 10 | √ | 0 |  |
| 28 | fchangebatch | fchangebatch | int4 | 32 |  | √ | 0 |  |
| 29 | fbatchqty | 最小包装量 | numeric | 23 | 10 | √ | 0 | 最小包装量 |
| 30 | fenabledate | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 31 | fwriteoffdirection | 冲销方向 | varchar | 30 |  | √ | ' ' | 冲销方向,枚举: A :向前冲销 B :向后冲销 C :向前向后冲销 D :向后向前冲销 |
| 32 | fpostprocessingtime | fpostprocessingtime | int4 | 32 |  | √ | 0 |  |
| 33 | freversalpriority | 冲销时间优先级 | varchar | 30 |  | √ | ' ' | 冲销时间优先级,枚举: A :预测优先 B :订单优先 |
| 34 | fintervalperiod | 分割间隔周期(天) | numeric | 23 | 10 | √ | 0 | 分割间隔周期(天) |
| 35 | fspecifiedperiod | 指定周期 | int8 | 64 |  | √ | 0 | [星空制造基础资料带组织模板 mpdm_mergecycle](../mpdm_files/mpdm_mergecycle.md) |
| 36 | fpreprocessingtime | fpreprocessingtime | int4 | 32 |  | √ | 0 |  |
| 37 | fdynamiccycle | 动态周期(天) | numeric | 23 | 10 | √ | 0 | 动态周期(天) |
| 38 | freservedtype | 预留类型 | varchar | 30 |  | √ | ' ' | 预留类型,枚举: 1 :强预留 0 :弱预留 |
| 39 | fdemandtimebound | 需求时界 | int4 | 32 |  | √ | 0 | 需求时界 |
| 40 | fforwardperiod | 向前冲销期间(天) | int4 | 32 |  | √ | 0 | 向前冲销期间(天) |
| 41 | fminlotsize | 最小订货量 | numeric | 23 | 10 | √ | 0 | 最小订货量 |
| 42 | fbatchincrement | 批量增量 | numeric | 23 | 10 | √ | 0 | 批量增量 |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_materialplan_e |  | fplanmode |
| 2 | pk_bd_materialplan_e |  | fid |

---

## 物料计划信息-多语言表 t_bd_materialplan_l

- **表名称：** 物料计划信息-多语言表
- **表名：** t_bd_materialplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_materialplan_l |  | fid,flocaleid |
| 2 | pk_bd_materialplan_l |  | fpkid |

---

## 物料计划信息-使用范围表 t_bd_materialplan_u

- **表名称：** 物料计划信息-使用范围表
- **表名：** t_bd_materialplan_u

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
| 1 | pk_t_bd_materialplan_u |  | fdataid,fuseorgid |
| 2 | idx_t_bd_materialplan_u_uo |  | fuseorgid |

---

## 物料计划信息-主表 t_bd_materialplan

- **表名称：** 物料计划信息-主表
- **表名：** t_bd_materialplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [BOM分组 mpdm_bomgroup](../mpdm_files/mpdm_bomgroup.md) |
| 3 | foperatorid | 计划员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmaterialid | 物料(冗余显示用_不支持逻辑处理) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | forgid | 管理组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmaterialgroupid | 物料控制组 | int8 | 64 |  | √ | 0 | [物料控制组 bd_materialcontrolgroup](../basedata_files/bd_materialcontrolgroup.md) |
| 7 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fadjustmentstrtegy | fadjustmentstrtegy | varchar | 30 |  | √ | ' ' |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fismrp | mrp | bpchar | 1 |  | √ | ' ' | mrp |
| 12 | fstatus | 计划信息数据状态 | varchar | 30 |  | √ | ' ' | 计划信息数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 15 | fbondcontrol | 保税控制 | bpchar | 1 |  | √ | '0' | 保税控制,枚举: 0 :非保税 1 :保税 2 :不控制 |
| 16 | fplangroupid | 计划组 | int8 | 64 |  | √ | 0 | [计划业务组 mpdm_demandgroup](../mpdm_files/mpdm_demandgroup.md) |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 19 | fxkallocationtype | 计划信息分配类型 | varchar | 30 |  | √ | ' ' | 计划信息分配类型,枚举: 1 :个性化 2 :共享型 |
| 20 | fplantagsid | 计划标识 | int8 | 64 |  | √ | 0 | [计划标识 mpdm_plantag](../mpdm_files/mpdm_plantag.md) |
| 21 | fmaterialattr | fmaterialattr | varchar | 30 |  | √ | ' ' |  |
| 22 | fcreateorgid | 计划信息创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fadjustbatchstrtegy | 调整考虑批量策略 | bpchar | 1 |  | √ | ' ' | 调整考虑批量策略 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fallowleadtime | 允许提前期间(天) | int4 | 32 |  |  | 0 | 允许提前期间(天) |
| 27 | fmbdmasterid | 物料计划信息内码 | int8 | 64 |  | √ | 0 | 物料计划信息内码 |
| 28 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fplantag | fplantag | varchar | 30 |  | √ | ' ' |  |
| 30 | fleadadvance | 提前容差(天) | int4 | 32 |  |  | 0 | 提前容差(天) |
| 31 | fcommoninfoid | 物料组织公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 32 | fctrlstrategy | 计划信息控制策略 | varchar | 30 |  | √ | ' ' | 计划信息控制策略,枚举: 2 :分配/局部共享 7 :私有 5 :全局共享 |
| 33 | fallowdelayperiod | 允许延后期间(天) | int4 | 32 |  |  | 0 | 允许延后期间(天) |
| 34 | fdelaytolerance | 延后容差(天) | int4 | 32 |  |  | 0 | 延后容差(天) |
| 35 | fenable | 计划信息使用状态 | varchar | 30 |  | √ | ' ' | 计划信息使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | fnumber | 编码 | varchar | 80 |  | √ | '' | 编码 |
| 37 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_materialplan_master |  | fmasterid |
| 2 | idx_t_bd_materialplansrcid |  | fsourcedataid |
| 3 | idx_t_bd_materialplanbit |  | fbitindex |
| 4 | idx_t_bd_materialplan_createorg |  | fcreateorgid |
| 5 | idx_bd_materialplan |  | fmasterid,fcreateorgid |
| 6 | idx_bd_materialplan_m1 |  | fmaterialid |
| 7 | pk_bd_materialplan |  | fid |
