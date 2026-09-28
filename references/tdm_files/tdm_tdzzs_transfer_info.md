# 转让信息-tdm_tdzzs_transfer_info

## 转让信息-主表 t_tdm_tdzzs_transfer_info

- **表名称：** 转让信息-主表
- **表名：** t_tdm_tdzzs_transfer_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flandtransferarea | 本次转让土地面积 | numeric | 23 | 10 | √ | 0 | 本次转让土地面积 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | ftransferremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 4 | fbuildingtransferarea | 本次转让建筑面积 | numeric | 23 | 10 | √ | 0 | 本次转让建筑面积 |
| 5 | ftransfercontractdate | 转让合同签订日期 | timestamp | 0 |  |  | null | 转让合同签订日期 |
| 6 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_tdzzs_transfer_in_1 |  | fid |
| 2 | pk_tdm_tdzzs_transfer_info |  | fentryid |
