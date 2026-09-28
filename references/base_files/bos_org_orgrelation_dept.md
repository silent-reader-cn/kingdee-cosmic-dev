# 业务单元分配部门-bos_org_orgrelation_dept

## 业务单元分配部门-主表 t_org_orgrelation

- **表名称：** 业务单元分配部门-主表
- **表名：** t_org_orgrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisincludesuborg | fisincludesuborg | bpchar | 1 |  | √ | '0' |  |
| 3 | fisincludesubtoorg | 受托包含下级 | bpchar | 1 |  | √ | '0' | 受托包含下级 |
| 4 | fisincludesubfromorg | 委托包含下级 | bpchar | 1 |  | √ | '0' | 委托包含下级 |
| 5 | fconddeleenabled | 启用条件委托 | bpchar | 1 |  | √ | '0' | 启用条件委托 |
| 6 | ftoorgid | 行政组织（部门） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fisdefaultfromorg | 是否默认委托组织 | bpchar | 1 |  | √ | '0' | 是否默认委托组织 |
| 8 | fisdefaulttoorg | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 9 | ftyperelationid | 协作关系类型 | int8 | 64 |  | √ | 0 | 业务协作关系 bos_org_typerelation |
| 10 | ffromorgid | 业务单元 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fxkenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 1 :可用 0 :禁用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_org_orgrelation_pkey |  | fid |
| 2 | idx_t_org_orgrelation_typefrom |  | ftyperelationid,ffromorgid |
