# 用户组继承关系-perm_usrgrp_inh

## 用户组继承关系-主表 t_perm_usrgrp_inh

- **表名称：** 用户组继承关系-主表
- **表名：** t_perm_usrgrp_inh

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fparentid | 被继承用户组ID | int8 | 64 |  | √ | 0 | 用户组 bos_usergroup |
| 4 | fchildrenid | 继承用户组ID | int8 | 64 |  | √ | 0 | 用户组 bos_usergroup |
| 5 | fcreatedatefield | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_perm_usrgrp_inh |  | fid |
| 2 | idx_perm_usrgrp_inh |  | fparentid |
