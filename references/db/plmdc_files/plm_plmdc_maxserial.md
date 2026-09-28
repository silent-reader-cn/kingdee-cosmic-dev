# 图号规则最大号-plm_plmdc_maxserial

## 图号规则最大号-主表 t_plmdc_maxserial

- **表名称：** 图号规则最大号-主表
- **表名：** t_plmdc_maxserial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdrawnorule | 图号规则 | int8 | 64 |  | √ | 0 | 图号规则列表 plm_plmdc_drawnorule |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fsortitemvalue | 流水号依据 | varchar | 50 |  | √ | ' ' | 流水号依据 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmaxserial | 最大流水号 | int8 | 64 |  | √ | 0 | 最大流水号 |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | finitserial | 初始流水号 | int8 | 64 |  | √ | 0 | 初始流水号 |
| 9 | fseqsegmententryid | 区间分段分录 | varchar | 50 |  | √ | ' ' | 区间分段分录 |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_maxserial |  | fdrawnorule |
| 2 | pk_t_plmdc_maxserial |  | fid |
