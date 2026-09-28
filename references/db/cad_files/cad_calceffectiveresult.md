# 生效卷算结果表-cad_calceffectiveresult

## 单据体-子表 t_cad_calceffectrsentry

- **表名称：** 单据体-子表
- **表名：** t_cad_calceffectrsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 耗用量 | numeric | 23 | 10 | √ | 0.0000000000 | 耗用量 |
| 3 | fsublot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 4 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 5 | fsubtracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 6 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | 资源维护(废弃) mpdm_resources |
| 7 | fsubcalcdimensionid | 成本卷算维度 | int8 | 64 |  | √ | 0 | 成本卷算维度 cad_calcdimension |
| 8 | fsubmatvers | 子项版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | factivityid | 工序活动 | int8 | 64 |  | √ | 0 | 工序活动定义(废弃) mpdm_processactivity |
| 11 | fsubkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | 卷算维度数据表 cad_keycol |
| 12 | felementid | 成本要素 | int8 | 64 |  | √ | 0 | 成本要素 cad_element |
| 13 | fcalcbasis | 计算依据 | varchar | 30 |  | √ | ' ' | 计算依据 |
| 14 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 15 | fstdprice | 标准成本 | numeric | 23 | 10 | √ | 0.0000000000 | 标准成本 |
| 16 | fsubkeycol | 维度字段 | varchar | 255 |  | √ | ' ' | 维度字段 |
| 17 | fsubconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 18 | fsubauxproperty | 子项辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 19 | fsubprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | fsubmaterialid | 子项物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fdatatype | 数据类别 | varchar | 30 |  | √ | ' ' | 数据类别,枚举: 1 :本层合计 2 :本级工费 3 :下级分项汇总 4 :直接下级按物料与子要素关系汇总 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_calceffectrsentry |  | fid,fresourceid |
| 2 | idx_cad_calceffectrsentry_kc |  | fsubkeycol |
| 3 | idx_cad_calceffectrsentry_dim |  | fsubcalcdimensionid |
| 4 | t_cad_calceffectrsentry_pkey |  | fentryid |
| 5 | indexcad_calceffectrsentry |  | felementid,fsubelementid,fsubmaterialid |

---

## 生效卷算结果表-主表 t_cad_calceffectiveresult

- **表名称：** 生效卷算结果表-主表
- **表名：** t_cad_calceffectiveresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprocessrouteid | 工艺路线 | int8 | 64 |  | √ | 0 | 分组基础资料带组织模板 cad_router |
| 3 | fsubelementid | fsubelementid | int8 | 64 |  | √ | 0 |  |
| 4 | fisleaf | 是否叶子节点 | varchar | 100 |  | √ | ' ' | 是否叶子节点,枚举: 0 :否 1 :是 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 7 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 8 | fprice | fprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 9 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 10 | freservedim2 | 预留2 | varchar | 100 |  | √ | ' ' | 预留2 |
| 11 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | fbomid | bom | int8 | 64 |  | √ | 0 | 分组基础资料带组织模板 cad_costbom |
| 13 | frootnode | 根节点 | varchar | 100 |  | √ | ' ' | 根节点 |
| 14 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 15 | ftreepath | 树路径 | varchar | 1000 |  | √ | ' ' | 树路径 |
| 16 | fispubmat | 是否公共件 | int8 | 64 |  | √ | 0 | 是否公共件 |
| 17 | fkeycolid | 卷算维度数据 | int8 | 64 |  | √ | 0 | 卷算维度数据表 cad_keycol |
| 18 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 19 | fqty | fqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 20 | fiscurrlevel | fiscurrlevel | varchar | 100 |  | √ | ' ' |  |
| 21 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fresourceid | fresourceid | int8 | 64 |  | √ | 0 |  |
| 23 | felementid | felementid | int8 | 64 |  | √ | 0 |  |
| 24 | fstdprice | fstdprice | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | fmatcostid | 物料成本信息ID | int8 | 64 |  | √ | 0 | 物料成本信息ID |
| 26 | flevel | 低阶码 | int8 | 64 |  | √ | 0 | 低阶码 |
| 27 | freservedim1 | 预留1 | varchar | 100 |  | √ | ' ' | 预留1 |
| 28 | fismaindata | 是否主数据 | int8 | 64 |  | √ | 0 | 是否主数据 |
| 29 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 30 | fmatvers | 版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 31 | fcalcdimensionid | 成本卷算维度 | int8 | 64 |  | √ | 0 | 成本卷算维度 cad_calcdimension |
| 32 | fkeycol | 维度字段 | varchar | 255 |  | √ | ' ' | 维度字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_calceffectiverst_df |  | fcosttypeid,fmaterialid,felementid,fsubelementid |
| 2 | idx_cad_calceffectiverst_kc |  | fkeycol |
| 3 | idx_cad_calceffectiverst_dim |  | fcalcdimensionid |
| 4 | t_cad_calceffectiveresult_pkey |  | fid |
