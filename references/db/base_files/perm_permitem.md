# 权限项-perm_permitem

## 权限项-多语言表 t_perm_permitem_l

- **表名称：** 权限项-多语言表
- **表名：** t_perm_permitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_perm_permitem_l_pkey |  | fpkid |
| 2 | ix_perm_00000012 |  | fid,flocaleid |

---

## 权限项-主表 t_perm_permitem

- **表名称：** 权限项-主表
- **表名：** t_perm_permitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 18 |  | √ | ' ' | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fgroup | 分类 | varchar | 50 |  | √ | ' ' | 分类,枚举: 10 :通用操作 20 :业务操作 |
| 4 | forder | forder | int8 | 64 |  | √ | 0 |  |
| 5 | finheritmode | 角色权限继承策略 | varchar | 10 |  | √ | ' ' | 角色权限继承策略,枚举: 10 :公有 20 :私有 |
| 6 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 7 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fbizdomainid | fbizdomainid | int8 | 64 |  | √ | 0 |  |
| 9 | fprepermitemid | 前置权限项 | varchar | 18 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 10 | fbizappid | 适用应用 | varchar | 18 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_permitem |  | fnumber |
| 2 | t_perm_permitem_pkey |  | fid |
