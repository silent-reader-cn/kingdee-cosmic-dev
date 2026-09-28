# 项目工作台页签定义-mpm_projecttag

## 项目工作台页签定义-主表 t_mpm_projecttag

- **表名称：** 项目工作台页签定义-主表
- **表名：** t_mpm_projecttag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 页签名称 | varchar | 255 |  | √ | ' ' | 页签名称 |
| 5 | ftabshoworder | 页签显示顺序 | int4 | 32 |  | √ | 0 | 页签显示顺序 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fpermitemid | 权限项 | varchar | 80 |  | √ | ' ' | [权限项 perm_permitem](../base_files/perm_permitem.md) |
| 8 | fauthbizobjectid | 授权业务对象 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 9 | fformtype | 页面类型 | bpchar | 1 |  | √ | ' ' | 页面类型,枚举: A :基础资料 B :单据 C :动态表单 D :列表 |
| 10 | fauthbizappid | 授权对象应用 | varchar | 80 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 11 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | foperationtype | 操作类型 | bpchar | 1 |  | √ | ' ' | 操作类型,枚举: A :新增 B :查看 C :编辑 |
| 17 | frelabusinessobjid | 关联业务对象 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 页签标识 | varchar | 80 |  | √ | ' ' | 页签标识 |
| 20 | fischeckchange | 是否校验变更 | bpchar | 1 |  | √ | '0' | 是否校验变更 |
| 21 | fisreload | 切换时重新加载 | bpchar | 1 |  | √ | '0' | 切换时重新加载 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_projecttag_number |  | fnumber |
| 2 | pk_mpm_projecttag |  | fid |

---

## 项目工作台页签定义-多语言表 t_mpm_projecttag_l

- **表名称：** 项目工作台页签定义-多语言表
- **表名：** t_mpm_projecttag_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fname | 页签名称 | varchar | 255 |  | √ | ' ' | 页签名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_projecttag_l |  | fpkid |
| 2 | idx_mpm_projecttag_l |  | fid,flocaleid |
