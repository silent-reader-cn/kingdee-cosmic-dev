# 消息中心菜单配置-msg_menuconfig

## 消息中心菜单配置-主表 t_wf_msgmenuconfig

- **表名称：** 消息中心菜单配置-主表
- **表名：** t_wf_msgmenuconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | fcategory | 分类 | varchar | 50 |  | √ | ' ' | 分类 |
| 4 | fmsgcentershow | 消息中心菜单是否展示 | bpchar | 1 |  | √ | '1' | 消息中心菜单是否展示 |
| 5 | fpersonalcentershow | 个人中心是否展示 | bpchar | 1 |  | √ | '1' | 个人中心是否展示 |
| 6 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 7 | fmsgtypeid | 长整数 | int8 | 64 |  | √ | 0 | 长整数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_msgmenuconfig_number |  | fnumber |
| 2 | pk_wf_msgmenuconfig |  | fid |

---

## 消息中心菜单配置-多语言表 t_wf_msgmenuconfig_l

- **表名称：** 消息中心菜单配置-多语言表
- **表名：** t_wf_msgmenuconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_msgmenuconfig_l |  | fid,flocaleid |
| 2 | pk_wf_msgmenuconfig_l |  | fpkid |
