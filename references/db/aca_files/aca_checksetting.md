# 盘点设置-aca_checksetting

## 盘点设置-主表 t_aca_checksetting

- **表名称：** 盘点设置-主表
- **表名：** t_aca_checksetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcheckcal | 盘点分配算法 | varchar | 30 |  | √ | 'inputout' | 盘点分配算法,枚举: inputout :按投入产量分配（有完工产品不承担） equivalent :按约当产量法下在产折算数量分配 |
| 3 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fchecktype | 盘点方式 | varchar | 30 |  | √ | 'qty' | 盘点方式,枚举: qty :数量 amount :金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aca_checksetting |  | fid |
| 2 | idx_aca_tchecksetting_org |  | forgid |
