# 业务应用菜单-bos_devportal_menu

## 业务应用菜单-多语言表 t_meta_bizappmenu_l

- **表名称：** 业务应用菜单-多语言表
- **表名：** t_meta_bizappmenu_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_bizappmenu_localeid |  | fid,flocaleid |
| 2 | t_meta_bizappmenu_l_pkey |  | fpkid |

---

## 业务应用菜单-主表 t_meta_bizappmenu

- **表名称：** 业务应用菜单-主表
- **表名：** t_meta_bizappmenu

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fparameter | 入口参数 | varchar | 300 |  | √ | ' ' | 入口参数 |
| 3 | fparentid | 上级菜单ID | varchar | 36 |  | √ | ' ' | 上级菜单ID |
| 4 | fvisible | 可见性 | bpchar | 1 |  | √ | ' ' | 可见性 |
| 5 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fdescription | fdescription | varchar | 500 |  | √ | ' ' |  |
| 8 | fcommon | fcommon | bpchar | 1 |  | √ | ' ' |  |
| 9 | fshortcutentrance | 快捷入口图标值 | varchar | 500 |  |  | null | 快捷入口图标值 |
| 10 | fbizappid | 应用ID | varchar | 36 |  | √ | ' ' | 应用ID |
| 11 | ficon | 图标 | varchar | 500 |  | √ | ' ' | 图标 |
| 12 | fpermission | 权限项 | varchar | 100 |  | √ | ' ' | 权限项 perm_permitem |
| 13 | fparametertype | 参数类型 | varchar | 50 |  | √ | ' ' | 参数类型,枚举: FormShowParameter :动态表单 BillShowParameter :单据 BaseShowParameter :基础资料 ListShowParameter :列表 ReportShowParameter :报表 ParameterShowParameter :参数 |
| 14 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 15 | fsimplenumber | 简码 | varchar | 20 |  | √ | ' ' | 简码 |
| 16 | fvectorimage | 矢量图值 | varchar | 500 |  | √ | ' ' | 矢量图值 |
| 17 | fopentype | 打开方式 | varchar | 5 |  | √ | '0' | 打开方式,枚举: 0 :默认 1 :弹窗 |
| 18 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 19 | ficonact | 激活图标 | varchar | 500 |  | √ | ' ' | 激活图标 |
| 20 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 22 | fformid | 页面ID | varchar | 36 |  | √ | ' ' | 页面ID |
| 23 | fformname | 页面 | varchar | 100 |  | √ | ' ' | 页面 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_bizappmenu_pkey |  | fid |
| 2 | idx_kdp_bizappmenu_num |  | fnumber |
