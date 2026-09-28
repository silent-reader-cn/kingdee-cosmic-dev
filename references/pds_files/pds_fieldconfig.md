# 字段页面配置-pds_fieldconfig

## 适用的页面配置方案-多选基础资料表 t_pds_compconfigs

- **表名称：** 适用的页面配置方案-多选基础资料表
- **表名：** t_pds_compconfigs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 组件页面配置 pds_compconfig |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_compconfigs |  | fpkid |
| 2 | idx_pds_compconfigs_bid |  | fbasedataid |
| 3 | idx_pds_compconfigs_fid |  | fid |

---

## 字段页面配置-主表 t_pds_fieldconfig

- **表名称：** 字段页面配置-主表
- **表名：** t_pds_fieldconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffield | 待更新字段(可多选) | varchar | 2000 |  | √ | ' ' | 待更新字段(可多选),枚举: |
| 9 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fcompid | 待更新组件 | int8 | 64 |  | √ | 0 | 组件注册 pds_compreg |
| 11 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_fieldconfig |  | fid |
| 2 | idx_pds_biddoc_content_cid |  | fcompid |
| 3 | idx_pds_biddoc_content_fnumber |  | fnumber |

---

## 字段分录-子表 t_pds_fieldconfigentry

- **表名称：** 字段分录-子表
- **表名：** t_pds_fieldconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcentryid | 页面配置分录id | int8 | 64 |  | √ | 0 | 页面配置分录id |
| 3 | fbiznodeid | 业务节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 4 | fdisplayname | 显示的名称 | bpchar | 50 |  | √ | ' ' | 显示的名称 |
| 5 | ffieldname | 字段名称 | varchar | 300 |  | √ | ' ' | 字段名称 |
| 6 | fismustinput | 是否必录 | bpchar | 1 |  | √ | '0' | 是否必录 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fiseditable | 是否可编辑 | bpchar | 1 |  | √ | '0' | 是否可编辑 |
| 9 | ffieldid | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 10 | fisvisible | 是否可见 | bpchar | 1 |  | √ | '0' | 是否可见 |
| 11 | fcompcfgid | 页面配置方案 | int8 | 64 |  | √ | 0 | 组件页面配置 pds_compconfig |
| 12 | fiswriteback | 是否可回写 | bpchar | 1 |  | √ | '0' | 是否可回写 |
| 13 | fisexport | 是否可引出 | bpchar | 1 |  | √ | '0' | 是否可引出 |
| 14 | fisclearup | 需要清空 | bpchar | 1 |  | √ | '0' | 需要清空 |
| 15 | fisimport | 是否可引入 | bpchar | 1 |  | √ | '0' | 是否可引入 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_fieldconfigentry_fid |  | fid |
| 2 | pk_pds_fieldconfigentry |  | fentryid |

---

## 字段页面配置-多语言表 t_pds_fieldconfig_l

- **表名称：** 字段页面配置-多语言表
- **表名：** t_pds_fieldconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pds_fieldconfig_l |  | fpkid |
| 2 | idx_pds_fieldconfig_l_fid |  | fid,flocaleid |
