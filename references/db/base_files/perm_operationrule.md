# 特殊数据权限规则-perm_operationrule

## 特殊数据权限规则-多语言表 t_perm_operationrule_l

- **表名称：** 特殊数据权限规则-多语言表
- **表名：** t_perm_operationrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_operationrule_l_pkey |  | fpkid |
| 2 | ix_perm_00000011 |  | fid,flocaleid |

---

## 特殊数据权限规则-主表 t_perm_operationrule

- **表名称：** 特殊数据权限规则-主表
- **表名：** t_perm_operationrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fispublic | 是否公有 | bpchar | 1 |  | √ | '0' | 是否公有,枚举: 1 :公有 0 :私有 |
| 3 | frule | 规则 | text | 0 |  |  | null | 规则 |
| 4 | foperationkey | 操作代码 | varchar | 30 |  | √ | ' ' | 操作代码 |
| 5 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 6 | foperationtype | 操作类型 | varchar | 30 |  | √ | ' ' | 操作类型 |
| 7 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 8 | fenabled | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 9 | fentitytypeid | 业务对象 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 10 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 11 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_operationrule |  | foperationtype,fentitytypeid |
| 2 | t_perm_operationrule_pkey |  | fid |
