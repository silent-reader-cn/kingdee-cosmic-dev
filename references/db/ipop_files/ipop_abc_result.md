# 入门必读用户学习统计-ipop_abc_result

## 入门必读用户学习统计-主表 t_ipop_abc_result

- **表名称：** 入门必读用户学习统计-主表
- **表名：** t_ipop_abc_result

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fuserid | 学习用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fitemid | 学习事项 | int8 | 64 |  | √ | 0 | 入门必读事项配置 ipop_abc_itemcfg |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_abc_result_item |  | fitemid |
| 2 | pk_t_ipop_abc_result |  | fid |
| 3 | idx_ipop_abc_result_user |  | fuserid |
