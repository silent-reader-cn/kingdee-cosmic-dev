# 吞吐量统计-isc_handcapacity

## 吞吐量统计-主表 t_isc_handcapacity

- **表名称：** 吞吐量统计-主表
- **表名：** t_isc_handcapacity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freceivehandcapacity | 接收吞吐量: | int8 | 64 |  | √ | 0 | 接收吞吐量: |
| 3 | fdate | 日期: | varchar | 100 |  | √ | ' ' | 日期: |
| 4 | fpushhandcapacity | 推送吞吐量: | int8 | 64 |  | √ | 0 | 推送吞吐量: |
| 5 | fallrunnumber | 总运行次数: | int8 | 64 |  | √ | 0 | 总运行次数: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_handcapacity_pkey |  | fid |
| 2 | idx_isc_handc_fdata |  | fdate |
