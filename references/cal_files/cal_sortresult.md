# 智能排序结果-cal_sortresult

## 单据体-子表 t_cal_sortresultentry

- **表名称：** 单据体-子表
- **表名：** t_cal_sortresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdividebasis | 划分依据 | varchar | 80 |  | √ | ' ' | 划分依据 |
| 3 | fstorageorgunitid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 5 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 8 | fdimensionkey | 成本域维度key | varchar | 255 |  | √ | ' ' | 成本域维度key |
| 9 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 10 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 11 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 货主 |
| 12 | fcaldimensionvalue | 核算维度值 | varchar | 225 |  | √ | ' ' | 核算维度值 |
| 13 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 14 | fassistid | 辅助属性 | int8 | 64 |  | √ | 0 | 辅助属性 |
| 15 | fcaldimension | 核算维度 | varchar | 80 |  | √ | ' ' | 核算维度 |
| 16 | fdividebasisvalue | 划分依据值 | varchar | 225 |  | √ | ' ' | 划分依据值 |
| 17 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 18 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fdimension | 成本域维度ID | int8 | 64 |  | √ | 0 | 成本域维度ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_sortresultentry_dimension |  | fdimension,fid |
| 2 | t_cal_sortresultentry_pkey |  | fentryid |
| 3 | idx_cal_sortrsentry_fid |  | fid |

---

## 智能排序结果-主表 t_cal_sortresult

- **表名称：** 智能排序结果-主表
- **表名：** t_cal_sortresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fheadcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | fgroupseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | faccounttype | 计价方法 | bpchar | 1 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 F :个别计价法 G :先进先出法 |
| 7 | fsortlistid | 排序链ID | int8 | 64 |  | √ | 0 | 排序链ID |
| 8 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 9 | fisloop | 是否循环 | bpchar | 1 |  | √ | '0' | 是否循环 |
| 10 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | 核算范围 cal_bd_calrange |
| 11 | fgroupno | 组别 | int8 | 64 |  | √ | '-1' | 组别 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_sortresult_material |  | fmaterialid |
| 2 | t_cal_sortresult_pkey |  | fid |
| 3 | idx_cal_sortresult_calorg |  | fheadcalorgid |
