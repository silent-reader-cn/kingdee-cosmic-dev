# 岗位汇报关系同步中间表_共享-xkds_postrelation_s

## 岗位汇报关系同步中间表_共享-主表 t_xkds_postrelation_s

- **表名称：** 岗位汇报关系同步中间表_共享-主表
- **表名：** t_xkds_postrelation_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsuperiorpostid | 上级岗位ID | int8 | 64 |  | √ | 0 | 上级岗位ID |
| 3 | fsuperiordept | 上级岗位所属部门 | varchar | 50 |  | √ | ' ' | 上级岗位所属部门 |
| 4 | fsuperiorpostnum | 上级岗位编码 | varchar | 80 |  | √ | ' ' | 上级岗位编码 |
| 5 | ftype | 数据类型 | varchar | 50 |  | √ | '0' | 数据类型,枚举: 0 :岗位汇报关系 1 :共享岗位汇报关系 |
| 6 | fcreatetime | 数据创建时间 | timestamp | 0 |  |  | null | 数据创建时间 |
| 7 | fpostnum | 岗位编码 | varchar | 80 |  | √ | ' ' | 岗位编码 |
| 8 | fdept | 岗位所属部门 | varchar | 50 |  | √ | ' ' | 岗位所属部门 |
| 9 | freporttype | 汇报类型 | varchar | 100 |  | √ | ' ' | 汇报类型 |
| 10 | fpostid | 岗位ID | int8 | 64 |  | √ | 0 | 岗位ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ds_relations_united |  | freporttype,fpostnum,fdept,fsuperiorpostnum,fsuperiordept |
| 2 | pk_xkds_postrelation_s |  | fid |
