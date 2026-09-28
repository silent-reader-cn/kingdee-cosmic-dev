# 单据类型参数升级工具-xkbilltypeparamupgrade

## 单据类型参数升级工具-主表 t_xkbilltypeparam_upgrade

- **表名称：** 单据类型参数升级工具-主表
- **表名：** t_xkbilltypeparam_upgrade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparameterfield | 参数字段 | varchar | 50 |  | √ | ' ' | 参数字段 |
| 3 | fparameterstatus | 执行状态 | varchar | 50 |  | √ | 'A' | 执行状态,枚举: A :暂存 B :执行成功 C :执行失败 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fparameterreturn | 执行结果 | varchar | 255 |  |  | ' ' | 执行结果 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 8 | fparameterreturn_tag | 执行结果_详情 | text | 0 |  |  | ' ' | 执行结果_详情 |
| 9 | fparametebilltypeid | 单据类型ID(0为全部) | varchar | 19 |  | √ | ' ' | 单据类型ID(0为全部) |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fparameterform | 更新的参数表单 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fparametervalue_tag | 参数json值_详情 | text | 0 |  |  | ' ' | 参数json值_详情 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fparameterexecutetime | 执行时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 执行时间 |
| 16 | fparametervalue | 参数json值 | varchar | 255 |  |  | ' ' | 参数json值 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbilltypeparam_upgrade |  | fid |
| 2 | id_paramtype_fparameterstatus |  | fparameterstatus |
