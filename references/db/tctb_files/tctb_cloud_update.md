# 云更新-tctb_cloud_update

## 云更新-主表 t_tctb_cloud_update

- **表名称：** 云更新-主表
- **表名：** t_tctb_cloud_update

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | foperaresult | 云更新结果 | varchar | 50 |  | √ | ' ' | 云更新结果,枚举: 0 :更新失败 1 :更新成功 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | foperatype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: 0 :云更新 1 :本地更新 |
| 8 | fbillno | 云更新编号 | varchar | 30 |  | √ | ' ' | 云更新编号 |
| 9 | fygxtime | 云更新时间 | timestamp | 0 |  |  | null | 云更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tctb_cloud_fbillno |  | fbillno |
| 2 | pk_tctb_cloud_update |  | fid |
