# 业务应用实体（规则引擎）-plm_rengine_bizapp

## 业务应用实体（规则引擎）-主表 t_meta_bizapp

- **表名称：** 业务应用实体（规则引擎）-主表
- **表名：** t_meta_bizapp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fmodeltype | fmodeltype | varchar | 50 |  | √ | 'AppModel' |  |
| 3 | fvisible | 可见性 | varchar | 5 |  | √ | '1' | 可见性 |
| 4 | fmainformid | 首页设置id | varchar | 36 |  | √ | ' ' | 首页设置id |
| 5 | fbizcloudid | 业务云 | varchar | 36 |  | √ | ' ' | [业务云 bos_devportal_bizcloud](../mdl_files/bos_devportal_bizcloud.md) |
| 6 | fseq | 序号 | int8 | 64 |  | √ | 1 | 序号 |
| 7 | fisv | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 8 | fmainformtype | 首页类型 | varchar | 5 |  | √ | '0' | 首页类型,枚举: 0 :表单 1 :外部链接 |
| 9 | fbackimage | 背景图片 | varchar | 500 |  | √ | ' ' | 背景图片 |
| 10 | falluserapp | 全员应用 | varchar | 5 |  | √ | '0' | 全员应用 |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fsimplenumber | 简码 | varchar | 20 |  | √ | ' ' | 简码 |
| 13 | fmasterid | 原厂应用id | varchar | 36 |  | √ | ' ' | 原厂应用id |
| 14 | fhomeurl | 链接地址 | varchar | 500 |  | √ | ' ' | 链接地址 |
| 15 | fopentype | 打开方式 | varchar | 5 |  | √ | '0' | 打开方式,枚举: 0 :新页签 1 :新窗口 2 :模态框 |
| 16 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | frefappid | 关联应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 19 | fusertype | 适用用户 | varchar | 500 |  | √ | '1' | 适用用户,枚举: 1 :职员 2 :客户 3 :供应商 4 :经销商 5 :其他伙伴 |
| 20 | fdata | 元数据内容 | text | 0 |  |  | null | 元数据内容 |
| 21 | findustry | 行业 | int8 | 64 |  | √ | 0 | [行业信息 bos_devp_industry](../devportal_files/bos_devp_industry.md) |
| 22 | fversion | 版本 | varchar | 100 |  | √ | ' ' | 版本 |
| 23 | fmainformname | 首页设置 | varchar | 100 |  | √ | ' ' | 首页设置 |
| 24 | fsubsysid | fsubsysid | int8 | 64 |  | √ | 0 |  |
| 25 | flabel | 标签 | varchar | 500 |  | √ | ' ' | 标签 |
| 26 | fparentid | 上级应用id | varchar | 36 |  | √ | ' ' | 上级应用id |
| 27 | fhelpurl | 帮助地址 | varchar | 300 |  | √ | ' ' | 帮助地址 |
| 28 | fsvnpath | svn地址 | varchar | 300 |  | √ | ' ' | svn地址 |
| 29 | fdeploystatus | 启用状态 | varchar | 5 |  | √ | '0' | 启用状态,枚举: 1 :未启用 2 :已启用 |
| 30 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fdescription | fdescription | varchar | 500 |  | √ | ' ' |  |
| 32 | finheritpath | 继承路径 | varchar | 300 |  | √ | ' ' | 继承路径 |
| 33 | forgfunc | 职能类型 | varchar | 5 |  | √ | ' ' | 职能类型,枚举: |
| 34 | ftype | 应用类型 | varchar | 5 |  | √ | '1' | 应用类型,枚举: 0 :原生 2 :扩展 |
| 35 | fdependencyid | 依赖应用id | varchar | 36 |  | √ | ' ' | 依赖应用id |
| 36 | fdbroute | 数据库标识 | varchar | 20 |  | √ | ' ' | 数据库标识,枚举: |
| 37 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 38 | fimage | 主题图片 | varchar | 500 |  | √ | ' ' | 主题图片 |
| 39 | fdependency | 依赖应用 | varchar | 500 |  | √ | ' ' | 依赖应用 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kdp_bizapp_masterid |  | fmasterid |
| 2 | idx_kdp_bizapp_visible |  | fvisible |
| 3 | t_meta_bizapp_pkey |  | fid |
| 4 | t_meta_bizapp_fnumber_key |  | fnumber |
| 5 | idx_kdp_bizapp_type |  | ftype |
| 6 | idx_kdp_bizapp_simpleenum |  | fsimplenumber |
| 7 | idx_kdp_bizapp_deploystatus |  | fdeploystatus |

---

## 业务应用实体（规则引擎）-多语言表 t_meta_bizapp_l

- **表名称：** 业务应用实体（规则引擎）-多语言表
- **表名：** t_meta_bizapp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 1024 |  | √ | ' ' | 描述 |
| 5 | fdata | fdata | text | 0 |  |  | null |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_meta_bizapp_l_pkey |  | fpkid |
| 2 | idx_kdp_bizapp_localeid |  | fid,flocaleid |
