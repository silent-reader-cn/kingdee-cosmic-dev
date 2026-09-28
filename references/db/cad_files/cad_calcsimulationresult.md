# 模拟卷算结果表-cad_calcsimulationresult

## 单据体-子表 t_cad_calcsimtreeentry

- **表名称：** 单据体-子表
- **表名：** t_cad_calcsimtreeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubcalcdate | 卷算时间 | timestamp | 0 |  |  | null | 卷算时间 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fsubroot | 根节点 | varchar | 100 |  | √ | ' ' | 根节点 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsubtreepath | 树路径 | varchar | 1200 |  | √ | ' ' | 树路径 |
| 7 | fsubcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_calcsimtreeentry |  | fentryid |
| 2 | idx_cad_calcsimtreeentry |  | fid |

---

## 单据体-子表 t_cad_calcsimularsentry

- **表名称：** 单据体-子表
- **表名：** t_cad_calcsimularsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 耗用数量 | numeric | 23 | 10 | √ | 0.0000000000 | 耗用数量 |
| 3 | fsublot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 4 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 5 | fsubtracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 6 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | [资源维护(废弃) mpdm_resources](../mpdm_files/mpdm_resources.md) |
| 7 | fsubcalcdimensionid | 成本卷算维度 | int8 | 64 |  | √ | 0 | [成本卷算维度 cad_calcdimension](../cad_files/cad_calcdimension.md) |
| 8 | fsubmatvers | 子项版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | factivityid | 工序活动 | int8 | 64 |  | √ | 0 | [工序活动定义(废弃) mpdm_processactivity](../mpdm_files/mpdm_processactivity.md) |
| 11 | fsubkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | [卷算维度数据表 cad_keycol](../cad_files/cad_keycol.md) |
| 12 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 13 | fcalcbasis | 计算依据 | varchar | 30 |  | √ | ' ' | 计算依据 |
| 14 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 15 | fstdprice | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 16 | fsubkeycol | 维度字段 | varchar | 255 |  | √ | ' ' | 维度字段 |
| 17 | fsubconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 18 | fsubauxproperty | 子项辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 19 | fsubprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 20 | fsubmaterialid | 子项物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fdatatype | 数据类别 | varchar | 30 |  | √ | ' ' | 数据类别,枚举: 1 :本层合计 2 :本级工费 3 :下级分项汇总 4 :直接下级按物料与子要素关系汇总 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_calcsimularsentry_dim |  | fsubcalcdimensionid |
| 2 | idx_cad_calcsimularsentry |  | fid,fresourceid |
| 3 | index_cad_calcsimularset_df |  | felementid,fsubelementid,fsubmaterialid |
| 4 | idx_cad_calcsimularsentry_kc |  | fsubkeycol |
| 5 | t_cad_calcsimularsentry_pkey |  | fentryid |

---

## 模拟卷算结果表-主表 t_cad_calcsimulars

- **表名称：** 模拟卷算结果表-主表
- **表名：** t_cad_calcsimulars

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprocessrouteid | 工艺路线 | int8 | 64 |  | √ | 0 | [分组基础资料带组织模板 cad_router](../basedata_files/cad_router.md) |
| 3 | fisleaf | 是否叶子节点 | varchar | 30 |  | √ | ' ' | 是否叶子节点,枚举: 0 :否 1 :是 |
| 4 | fmaterielid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 6 | freservedim2 | 预留2 | varchar | 100 |  | √ | ' ' | 预留2 |
| 7 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fbomid | bom | int8 | 64 |  | √ | 0 | [分组基础资料带组织模板 cad_costbom](../basedata_files/cad_costbom.md) |
| 9 | frootnode | 根节点 | varchar | 100 |  | √ | ' ' | 根节点 |
| 10 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 11 | ftreepath | 树路径 | varchar | 1200 |  | √ | ' ' | 树路径 |
| 12 | fispubmat | 是否公共件 | int8 | 64 |  | √ | 0 | 是否公共件 |
| 13 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | [卷算维度数据表 cad_keycol](../cad_files/cad_keycol.md) |
| 14 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 15 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 16 | fcalcdate | 卷算日期 | timestamp | 0 |  |  | null | 卷算日期 |
| 17 | fiscalccurlevel | 是否只计算本层物料 | int4 | 32 |  | √ | 0 | 是否只计算本层物料 |
| 18 | flevel | 低阶码 | int8 | 64 |  | √ | 0 | 低阶码 |
| 19 | freservedim1 | 预留1 | varchar | 100 |  | √ | ' ' | 预留1 |
| 20 | fismaindata | 是否主数据 | int8 | 64 |  | √ | 0 | 是否主数据 |
| 21 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 22 | fmatvers | 版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 23 | fcalcdimensionid | 成本卷算维度 | int8 | 64 |  | √ | 0 | [成本卷算维度 cad_calcdimension](../cad_files/cad_calcdimension.md) |
| 24 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 25 | fkeycol | 维度字段 | varchar | 255 |  | √ | ' ' | 维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_calcsimulars_df |  | fcosttypeid,fmaterielid,fauxproperty,fmatvers |
| 2 | idx_cad_calcsimulars_dim |  | fcalcdimensionid |
| 3 | t_cad_calcsimulars_pkey |  | fid |
| 4 | idx_cad_calcsimulars_kc |  | fkeycol |
