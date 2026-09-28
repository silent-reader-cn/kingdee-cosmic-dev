# 用户完工差异率偏差范围设置-sca_userfinishoffset

## 用户完工差异率偏差范围设置-主表 t_sca_userfinishoffset

- **表名称：** 用户完工差异率偏差范围设置-主表
- **表名：** t_sca_userfinishoffset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frightoffset | 右偏差 | numeric | 23 | 10 | √ | 0.0000000000 | 右偏差 |
| 3 | foffsetrate | 偏差率 | numeric | 23 | 10 | √ | 0.0000000000 | 偏差率 |
| 4 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fleftoffset | 左偏差 | numeric | 23 | 10 | √ | 0.0000000000 | 左偏差 |
| 6 | fdifftype | 差异类型 | varchar | 30 |  | √ | '1' | 差异类型,枚举: 1 :物料子要素 2 :全部子要素 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_userfinishoffset_pkey |  | fid |
| 2 | index_sca_userfinishoffset |  | fuserid,fdifftype |
