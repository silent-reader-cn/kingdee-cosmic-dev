# 元素属性-bos_devp_properpty

## 元素属性-多语言表 t_dm_property_l

- **表名称：** 元素属性-多语言表
- **表名：** t_dm_property_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 50 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dm_property_l |  | fid,flocaleid |
| 2 | pk_t_dm_property_l |  | fpkid |

---

## 元素属性-主表 t_dm_property

- **表名称：** 元素属性-主表
- **表名：** t_dm_property

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxml | 详情 | varchar | 255 |  | √ | ' ' | 详情 |
| 3 | fgroupid | 所属分组 | varchar | 50 |  |  | null | 所属分组,枚举: 1 :常用属性 2 :基础设置 3 :高级属性 4 :基本信息 5 :其它 6 :常用样式 7 :风格属性 8 :风格属性 9 :高级样式 10 :高级样式 11 :高级设置 12 :顶部导航页签 13 :顶部基本信息 15 :不可见 |
| 4 | ftype | 类型 | varchar | 50 |  |  | null | 类型,枚举: text :文本 dimension :尺寸 checkbox :复选框 integer :整型 color :颜色 btnedit :复杂对象 combo :下拉列表 mcombo :多选下拉列表 refcombo :引用下拉列表 ecombo :元素下拉列表 date :日期 daterange :日期范围 decimal :精度 position :位置 radius :圆角 |
| 5 | fisv | 开发商标识 | varchar | 50 |  |  | null | 开发商标识 |
| 6 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 7 | fxml_tag | 详情_详情 | text | 0 |  |  | null | 详情_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dm_property |  | fid |
| 2 | idx_t_dm_property |  | fnumber |
