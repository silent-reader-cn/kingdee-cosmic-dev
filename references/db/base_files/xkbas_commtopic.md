# 社区专题-xkbas_commtopic

## 社区专题-主表 t_xkbas_commtopic

- **表名称：** 社区专题-主表
- **表名：** t_xkbas_commtopic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxkdata | 接口数据 | text | 0 |  |  | null | 接口数据 |
| 3 | fxktype | 接口类型 | varchar | 50 |  | √ | ' ' | 接口类型,枚举: 1 :专题列表 2 :专题详情 3 :专题视频 |
| 4 | fxkcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fxkkey | 接口标识 | varchar | 255 |  | √ | ' ' | 接口标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_xkbas_commtopic_xkkey |  | fxkkey |
| 2 | pk_t_xkbas_commtopic |  | fid |
