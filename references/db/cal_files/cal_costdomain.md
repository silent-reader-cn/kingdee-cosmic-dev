# 成本域维度-cal_costdomain

## 成本域维度-主表 t_cal_costdomain

- **表名称：** 成本域维度-主表
- **表名：** t_cal_costdomain

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdividebasis | 划分依据 | varchar | 255 |  | √ | ' ' | 划分依据 |
| 3 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 4 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目号 pur_project |
| 5 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcaldimensionval | 核算维度值 | varchar | 255 |  | √ | ' ' | 核算维度值 |
| 8 | fdimensionkey | 维度key | varchar | 50 |  | √ | ' ' | 维度key |
| 9 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 10 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 11 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 12 | fcalrangeid | 核算范围 | int8 | 64 |  | √ | 0 | 核算范围 cal_bd_calrange |
| 13 | fstorageunitid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 16 | fdividebasisval | 划分依据值 | varchar | 255 |  | √ | ' ' | 划分依据值 |
| 17 | faccounttype | 计价方法 | varchar | 1 |  | √ | ' ' | 计价方法,枚举: A :加权平均法 B :移动平均法 F :个别计价法 G :先进先出法 |
| 18 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 19 | fcaldimension | 核算维度 | varchar | 255 |  | √ | ' ' | 核算维度 |
| 20 | flot | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 21 | fassit | 辅助属性 | int8 | 64 |  | √ | 0 | 辅助属性 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cal_costdomain |  | fid |
| 2 | idx_cal_costdomain_cpm |  | fcostaccountid,fperiodid,fmaterialid |
| 3 | idx_cal_costdomain_dkey |  | fdimensionkey |
