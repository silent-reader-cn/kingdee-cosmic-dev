# 记录多选下拉项-arm_chartdisplay_record

## 记录多选下拉项-主表 t_arm_chartdisplay

- **表名称：** 记录多选下拉项-主表
- **表名：** t_arm_chartdisplay

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmastermaterialid | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 2 | fproductionlineid | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 3 | fchartdisplay | 多选下拉项 | varchar | 250 |  | √ | ' ' | 多选下拉项 |
| 4 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 5 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 6 | fmaterialno | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 7 | fstartdate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | freporttype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型 |
| 9 | fworkshop | 车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fleadtimes | 前置时段（天） | int8 | 64 |  | √ | 0 | 前置时段（天） |
| 11 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 12 | forg | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_arm_chartdisplay_m0 |  | freporttype |
| 2 | pk_arm_chartdisplay |  | fid |
