# 自定义权限服务注册-perm_custompermserv

## 自定义权限服务注册-主表 t_perm_custpermserv

- **表名称：** 自定义权限服务注册-主表
- **表名：** t_perm_custpermserv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmethodname | fmethodname | varchar | 255 |  | √ | ' ' |  |
| 3 | fservfactory | 服务工程类 | varchar | 200 |  | √ | ' ' | 服务工程类 |
| 4 | fservappnum | 微服务所在应用编码 | varchar | 60 |  | √ | ' ' | 微服务所在应用编码 |
| 5 | fscenarioid | fscenarioid | int8 | 64 |  | √ | 0 |  |
| 6 | fservname | 服务接口名 | varchar | 200 |  | √ | ' ' | 服务接口名 |
| 7 | fisand | 执行结果和平台结果是否取交集 | bpchar | 1 |  | √ | '0' | 执行结果和平台结果是否取交集 |
| 8 | fisskip | 是否跳过 | bpchar | 1 |  | √ | '0' | 是否跳过 |
| 9 | fappid | 应用 | varchar | 60 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_custpermserv |  | fappid |
| 2 | t_perm_custpermserv_pkey |  | fid |
