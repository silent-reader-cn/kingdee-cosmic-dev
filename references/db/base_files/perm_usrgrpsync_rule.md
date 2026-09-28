# 用户组人员同步规则-perm_usrgrpsync_rule

## 用户组人员同步规则-主表 t_perm_usrgrprel_ruleent

- **表名称：** 用户组人员同步规则-主表
- **表名：** t_perm_usrgrprel_ruleent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fruleconftype | 规则配置方式 | varchar | 50 |  | √ | ' ' | 规则配置方式,枚举: 1 :按人员属性配置 2 :自定义配置 |
| 4 | fuserfieldkey | 用户字段 | varchar | 50 |  | √ | ' ' | 用户字段 |
| 5 | foper | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fsrcentity | 数据源实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | frule | 规则 | text | 0 |  |  | null | 规则 |
| 10 | fusrgrpid | 用户组 | int8 | 64 |  | √ | 0 | [用户组 bos_usrgrp](../base_files/bos_usrgrp.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fgrprefbdtype | 分组基础资料类型 | varchar | 50 |  | √ | ' ' | 分组基础资料类型 |
| 13 | fgrpreffieldkey | 分组字段 | varchar | 50 |  | √ | ' ' | 分组字段 |
| 14 | frule_tag | 规则_详情 | text | 0 |  |  | null | 规则_详情 |
| 15 | fiscomplexrule | 复杂规则 | bpchar | 1 |  | √ | '0' | 复杂规则 |
| 16 | fgrprefvalue | 分组字段值 | varchar | 500 |  | √ | ' ' | 分组字段值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_perm_usrgrprel_ruleent |  | fid |
| 2 | idx_perm_usrgrprel_ruent |  | fusrgrpid |
