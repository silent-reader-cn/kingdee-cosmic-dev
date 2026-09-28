# 组件页面配置-pds_compconfig

## 组件页面配置-主表 t_pds_compconfig

- **表名称：** 组件页面配置-主表
- **表名：** t_pds_compconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | fpurchaserid | 采购员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fname | 方案名称 | varchar | 300 |  | √ | ' ' | 方案名称 |
| 6 | fpurdept | 采购部门 | int8 | 64 |  | √ | 0 | 采购部门 pds_purdepart |
| 7 | fbiznodeid | 业务节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fsrctypeld | 招标流程 | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 13 | foperate | 必录校验操作 | varchar | 30 |  | √ | ' ' | 必录校验操作,枚举: |
| 14 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcomponentid | 业务组件 | int8 | 64 |  | √ | 0 | 组件注册 pds_compreg |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fvalidatorplugin | 必录校验插件 | varchar | 225 |  | √ | ' ' | 必录校验插件 |
| 19 | fsourcetypeid | 寻源方式 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 22 | fsourceclassid | 招标方式类型 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 23 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 24 | fnegotiatetype | 议价方式 | bpchar | 1 |  | √ | ' ' | 议价方式,枚举: 1 :线上议价 2 :线下议价(标的) 4 :电子竞价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_compconfig |  | fid |
| 2 | idx_pds_compconfig_fclass |  | fsourceclassid |
| 3 | idx_pds_compconfig_fnumber |  | fnumber |
| 4 | idx_pds_compconfig_ftype |  | fsourcetypeid |
| 5 | idx_pds_compconfig_fmasterid |  | fmasterid |
| 6 | idx_pds_compconfig_fsrctype |  | fsrctypeld |
| 7 | idx_pds_compconfig_fbiznode |  | fbiznodeid |

---

## 组件页面配置-多语言表 t_pds_compconfig_l

- **表名称：** 组件页面配置-多语言表
- **表名：** t_pds_compconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 300 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_compconfig_l |  | fpkid |
| 2 | idx_pds_compconfig_l_fid |  | fid,flocaleid |
| 3 | idx_pds_compconfig_l_name |  | fname |

---

## 字段分录-子表 t_pds_compconfigentry

- **表名称：** 字段分录-子表
- **表名：** t_pds_compconfigentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdisplayname | 显示的名称 | varchar | 50 |  | √ | ' ' | 显示的名称 |
| 3 | ffieldname | 字段名称 | varchar | 300 |  | √ | ' ' | 字段名称 |
| 4 | fismustinput | 是否必录 | bpchar | 1 |  | √ | '0' | 是否必录 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fiseditable | 是否可编辑 | bpchar | 1 |  | √ | '0' | 是否可编辑 |
| 7 | ffieldid | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 8 | fisvisible | 是否可见 | bpchar | 1 |  | √ | '0' | 是否可见 |
| 9 | fiswriteback | 是否可回写 | bpchar | 1 |  | √ | '0' | 是否可回写 |
| 10 | fisexport | 是否可引出 | bpchar | 1 |  | √ | '0' | 是否可引出 |
| 11 | fisclearup | 需要清空 | bpchar | 1 |  | √ | '0' | 需要清空 |
| 12 | fisimport | 是否可引入 | bpchar | 1 |  | √ | '0' | 是否可引入 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_compconfigentry |  | fentryid |
| 2 | idx_pds_compconfigentry_fid |  | fid |
