# 物料主数据信息归档-cad_stdcalcmatfiltersava

## 物料主数据信息归档-主表 t_cad_stdcalcmatfiltersv

- **表名称：** 物料主数据信息归档-主表
- **表名：** t_cad_stdcalcmatfiltersv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmatfilter | 物料主数据信息 | varchar | 2000 |  | √ | ' ' | 物料主数据信息 |
| 3 | fmatfilter_tag | 物料主数据信息_详情 | text | 0 |  |  | null | 物料主数据信息_详情 |
| 4 | fisstdcostmat | 计算使用标准成本计价法的物料 | bpchar | 1 |  | √ | '1' | 计算使用标准成本计价法的物料 |
| 5 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_stdcalcmatfiltersv |  | fuserid |
| 2 | pk_t_cad_stdcalcmatfiltersv |  | fid |
