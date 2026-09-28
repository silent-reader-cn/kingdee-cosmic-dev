# IPD页面配置-plm_ipdpagecfg

## 单据体-多语言表 t_plm_ipdpagecfgentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_plm_ipdpagecfgentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | flablename | 标签名称 | varchar | 399 |  |  | ' ' | 标签名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipdpagecfgentry_l |  | fpkid |
| 2 | idx_plm_ipdpagecfgentry_l_0 |  | fentryid,flocaleid |

---

## 单据体-子表 t_plm_ipdpagecfgentry

- **表名称：** 单据体-子表
- **表名：** t_plm_ipdpagecfgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcfgstate | 启用 | varchar | 50 |  | √ | ' ' | 启用,枚举: Q :启用 J :禁用 |
| 3 | fpageid | 子页面 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 4 | fpermimp | 页面插件 | varchar | 255 |  | √ | ' ' | 页面插件 |
| 5 | fpagetype | 页面类型 | varchar | 50 |  | √ | ' ' | 页面类型,枚举: form :表单 list :列表 |
| 6 | fpagetpl | 页面模版 | varchar | 255 |  | √ | ' ' | 页面模版 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | flable | 标签 | varchar | 255 |  |  | ' ' | 标签 |
| 10 | ftarget | 容器标识 | varchar | 255 |  |  | ' ' | 容器标识 |
| 11 | flablename | 标签名称 | varchar | 255 |  |  | ' ' | 标签名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipdpagecfgentry |  | fentryid |
| 2 | idx_plm_ipdpagecfgentry_fk |  | fid |

---

## IPD页面配置-主表 t_plm_ipdpagecfg

- **表名称：** IPD页面配置-主表
- **表名：** t_plm_ipdpagecfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fdefaulttarget | 默认容器标识 | varchar | 50 |  | √ | ' ' | 默认容器标识 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 6 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | ftarpageid | 主页面 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 20 | fuselever | 应用层级 | varchar | 50 |  | √ | ' ' | 应用层级,枚举: 0 :同页面扩展 1 :子页面 2 :二级子页面 |
| 21 | fshowtype | 页面呈现方式 | varchar | 50 |  | √ | ' ' | 页面呈现方式,枚举: 0 :default 1 :newtabpage 3 :incontainer 4 :float 5 :nonmodal 6 :modal 7 :mainnewtabpage 8 :incurrentform 9 :floatingautohide 10 :newwindow 11 :inframe |
| 22 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_ipdpagecfg_createorg |  | fcreateorgid |
| 2 | idx_t_plm_ipdpagecfg_master |  | fmasterid |
| 3 | idx_plm_ipdpagecfg_m0 |  | fmasterid |
| 4 | pk_plm_ipdpagecfg |  | fid |

---

## IPD页面配置-多语言表 t_plm_ipdpagecfg_l

- **表名称：** IPD页面配置-多语言表
- **表名：** t_plm_ipdpagecfg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_ipdpagecfg_l_0 |  | fid,flocaleid |
| 2 | pk_plm_ipdpagecfg_l |  | fpkid |

---

## IPD页面配置-使用范围表 t_plm_ipdpagecfg_u

- **表名称：** IPD页面配置-使用范围表
- **表名：** t_plm_ipdpagecfg_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_ipdpagecfg_u |  | fdataid,fuseorgid |
| 2 | idx_t_plm_ipdpagecfg_u_uo |  | fuseorgid |

---

## 子单据体-子表 t_plm_ipdpagecfgfield

- **表名称：** 子单据体-子表
- **表名：** t_plm_ipdpagecfgfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsourcefield | 原字段 | varchar | 255 |  |  | ' ' | 原字段 |
| 2 | ffieldtype | 字段来源 | varchar | 50 |  | √ | ' ' | 字段来源,枚举: parent :父页面 showParameter :页面显示参数 customParams :自定义参数 |
| 3 | ftargetfield | 映射字段 | varchar | 255 |  |  | ' ' | 映射字段 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fcombofield | 映射字段处理方式 | varchar | 50 |  | √ | ' ' | 映射字段处理方式,枚举: showAndFilter :页面显示并过滤 show :仅仅做页面显示 showParameter :放到自定义参数 innerParameter :页面自带参数 |
| 8 | ftextfield | 字段值 | varchar | 255 |  |  | ' ' | 字段值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipdpagecfgfield |  | fdetailid |
| 2 | idx_plm_ipdpagecfgfield_fk |  | fentryid |
