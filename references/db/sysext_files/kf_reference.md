# 引用关系-kf_reference

## 引用关系-主表 t_kf_reference

- **表名称：** 引用关系-主表
- **表名：** t_kf_reference

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fevent | 事件 | varchar | 50 |  | √ | ' ' | 事件 |
| 3 | ftriggertime | 触发时机 | varchar | 50 |  | √ | ' ' | 触发时机,枚举: 5 :创建，值更新 3 :加载，值更新 4 :创建 2 :加载 1 :值更新 0 :- |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fresourceid | 业务对象 | varchar | 50 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 6 | fappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 7 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 8 | fkfid | K流 | int8 | 64 |  | √ | 0 | [实例 kf_instance](../sysext_files/kf_instance.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fscene | 引用场景 | varchar | 36 |  | √ | ' ' | 引用场景,枚举: rule :规则 operate :操作 |
| 12 | fdesc | 描述 | varchar | 200 |  | √ | ' ' | 描述 |
| 13 | fdata | 配置 | text | 0 |  |  | null | 配置 |
| 14 | fenabled | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 1 :启用 0 :禁用 A :创建 B :审核中 C :已审核 D :重新审核 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_kf_reference |  | fid |
| 2 | idx_kf_ref_resourceid |  | fresourceid |
| 3 | idx_kf_ref_kfid |  | fkfid |
